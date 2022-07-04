project_name=leech
ci_cd_path=ci_cd
PG_NAME=geo_db
HUB_USER=eronlivramento
HUB_HOST=hub.docker.com/repository/docker
VERSION ?= latest
IMAGE = ${HUB_USER}/${project_name}:$(VERSION)
compose_run=POSTGRES_NAME=${PG_NAME} IMAGE=${IMAGE} docker-compose run

check-version:
	@ if [ "${VERSION}" = "latest"  ]; then \
		echo "The release VERSION variable can not be latest"; \
		exit 1; \
	fi

image:
	docker build -t $(IMAGE) .

shell: image
	$(compose_run) ${project_name} sh

logs-%:
	docker-compose logs $*

env: stop-env image
	IMAGE=${IMAGE} \
	POSTGRES_NAME=${PG_NAME} \
	docker-compose up -d

stop-env:
	POSTGRES_NAME=${PG_NAME} IMAGE=${IMAGE} docker-compose down -v

clean: stop-env
	docker-compose rm -f -v

tests: stop-env image
	$(compose_run) --rm ${project_name} ./${ci_cd_path}/tests.sh

integration-tests: stop-env image
	$(compose_run) --rm ${project_name} ./${ci_cd_path}/integration-tests.sh

format-check: stop-env image
	$(compose_run) --rm ${project_name} ./${ci_cd_path}/format-check.sh

style-check: stop-env image
	$(compose_run) --rm ${project_name} ./${ci_cd_path}/style-check.sh

install-lint-requirements:
	./${ci_cd_path}/install-lint-requirements.sh

black:
	./${ci_cd_path}/black-format.sh

check-all: format-check style-check

test-all: tests integration-tests

push-docker: check-version
	docker push $(IMAGE)

release: push-docker
	git tag -a $(VERSION) -m "Release automatically generated "$(VERSION)
	git push origin $(VERSION)

run-local: env
	python3 src/cmd/${project_name}.py

run-local-docker: stop-env image
	$(compose_run) ${project_name} ./${ci_cd_path}/run-docker.sh
