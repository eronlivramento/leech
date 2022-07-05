from src.infrastructure.environment.environment import Env


class ConfigManager:
    def __init__(self, mongo_client) -> None:
        self.mongo_client = mongo_client
        self.env = Env()

    def get_configs_from_mongo(self) -> list:
        db = self.mongo_client[self.env.get_configs_db()]
        sources = db["sources"]

        return [source for source in sources.find()]
