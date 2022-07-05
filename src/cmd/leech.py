import os
from src.app.application import Application
from src.infrastructure.datasources.postgres.postgres import PostgreSQL
from src.infrastructure.datasources.mongodb.mongodb import MongoDb
from src.infrastructure.datasources.repository.repository import Repository
from src.infrastructure.environment.environment import Env
from src.sources.configs.config_manager import ConfigManager


if __name__ == "__main__":
    env = Env()
    mongo = MongoDb(
        env.get_mongo_user(),
        env.get_mongo_password(),
        env.get_mongo_host(),
        env.get_mongo_port(),
    )
    config_manager = ConfigManager(mongo_client=mongo.connect())
    configs = config_manager.get_configs_from_mongo()

    for source in configs:
        source_name = source["name"]
        print(f"Capturing source: {source_name}")

        if source_name != "dummy":
            source_url = source["url"]
            db_host = os.getenv(source["env_db_host"])
            db_port = os.getenv(source["env_db_port"])
            db_name = os.getenv(source["env_db_name"])
            db_schema = os.getenv(source["env_db_schema"])
            input_table = os.getenv(source["env_input_table"])
            input_fields = source["input_fields"]
            scrapy_path = source["scrapy_path"]
            db_user = os.getenv(source["env_db_user"])
            db_pass = os.getenv(source["env_db_password"])

            pg = PostgreSQL(
                host=db_host,
                port=db_port,
                database=db_name,
                user=db_user,
                password=db_pass,
            )
            conn = pg.connect()
            app = Application(
                source_url,
                Repository(conn, db_schema, input_table, input_fields),
                scrapy_path,
            )
            app.run()
            app.export()
            conn.close()
