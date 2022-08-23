import os
from src.infrastructure.environment.environment import Env

config_manager = Env()


class TestEnv:
    def test_get_env_found(self):
        os.environ["ENV_VAR_TEST"] = "FOUND"
        assert config_manager.get_env("ENV_VAR_TEST") == "FOUND"
        os.environ["ENV_VAR_TEST"] = ""

    def test_get_env_not_found(self):
        assert config_manager.get_env("ENV_VAR_TEST") == "env not set"

    def test_get_env_default_value(self):
        assert config_manager.get_env("ENV_VAR_TEST", "default") == "default"
