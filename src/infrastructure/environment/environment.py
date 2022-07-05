import os


class Env:
    def get_env(self, var: str, default_value: str = "") -> str:
        result = os.getenv(var)
        if result != "" and result is not None:
            return result

        if default_value != "":
            return default_value

        return "env not set"

    def get_mongo_user(self) -> str:
        return self.get_env("MONGO_USER", "mongouser")

    def get_mongo_password(self) -> str:
        return self.get_env("MONGO_PASSWORD", "password")

    def get_configs_db(self) -> str:
        return self.get_env("MONGO_CONFIGS_DB", "configs")

    def get_mongo_host(self) -> str:
        return self.get_env("MONGO_HOST", "mongo")

    def get_mongo_port(self) -> int:
        return int(self.get_env("MONGO_PORT", "27017"))
