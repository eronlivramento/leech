# Leech

Leech is a project responsible to get data from web based on sources configuration.

![alt text](/doc/static/img/sequence_diagram.png)

# Running Locally

## Running without Docker

Before running it locally with python3 command, you must set some environment variables as follows:

#### Environment Variables

```
export GEO_HOST=localhost
export GEO_PORT=5434
export GEO_DATABASE=geo
export GEO_USER=postgres
export GEO_PASSWORD=admin
export GEO_SCHEMA=geolocation
export CEP_INPUT_TABLE=ceps_range
export MONGO_USER=mongouser
export MONGO_PASSWORD=password
export MONGO_CONFIGS_DB=configs
export MONGO_HOST=localhost
export MONGO_PORT=27017
```

To run this code without docker run the following command:

```
make run-local
```

#### Stop environment

To manually stop the environment you can run the following command:

```
make stop-env
```

## Running with docker

```
make run-local-docker
```

# Check Code Style

Before commit to this project, make sure you have checked and formated everything with the following commands.

## Check code format, indentation, etc

```
make format-check
```

## Check against [PEP8](https://peps.python.org/pep-0008/) style

```
make style-check
```

## Check all

```
make check all
```

## Format code before commit
Before run the make command, make sure you have installed the lint requirements as follows:
```
make install-lint-requirements
```

```
make black
```

# Testing

## Unit

In orther to unit test you can run the following command:


```
make tests
```

## Integration

In orther to run the integration tests run the following command:

```
make integration-tests
```

## Run all tests

If you want to run all tests at once you can run the following command:

```
make test-all
```

# Generating a New Release

After merging your Merge Request to the master branch, you can generate and push a new release image to docker hub by running the following command:

```
make release VERSION=1.0.0
```

Replace ‘1.0.0’ with the version you want to release.

# Test evaluation notes

This section aims to make the evaluation process easier.

However, you can evaluate this screening process test the following instructions below.

```
make run-local-docker
```

# Result in Postgress database

result of this application is persisted in the database postgress, if you want check the result on database following instructions below
After running the application, access postgress, select the geo schema and run the following query

```
SELECT * FROM geolocation.ceps_range
```