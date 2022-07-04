from pymongo import MongoClient


class MongoDb:
    def __init__(self, user: str, password: str, host: str, port: str) -> None:
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def connect(self):
        try:
            return MongoClient(
                f"mongodb://{self.user}:{self.password}@{self.host}:{self.port}"
            )
        except Exception as e:
            raise e
