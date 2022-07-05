import json

from src.model.cep_range import CepRangeModel
from src.scrapy.handler import Handler
from src.scrapy.scrapy import Scrapy


class Application:
    def __init__(self, url: str, repository, paths):
        self.scrapy = Scrapy(url)
        self.handler = Handler()
        self.repository = repository
        self.paths = paths

    def run(self):
        """
        Method that starts capturing data.
        """
        print("Application init...")

        self.scrapy.start()
        data = self.scrapy.get_element_text(self.paths["field_list"])
        data_list = data.rsplit("\n")
        for data in data_list:
            if data.strip() == "":
                continue

            print(f"Getting data in {data}")
            self.__execute__(data)

            self.scrapy.click(self.paths["back_form"])

        self.scrapy.quit()

    def __execute__(self, data):
        self.scrapy.select_option(self.paths["select_option"], data)
        self.scrapy.click(self.paths["submit_form"])

        table = self.__get_list_dict__(self.paths["data_capture"])
        self.__save__(data, table)

        while self.scrapy.check_if_exist(self.paths["has_navegation"]):
            self.scrapy.click(self.paths["navegation"])
            data_capture = self.paths["data_capture_navegation"]
            table = self.__get_list_dict__(data_capture)
            self.__save__(data, table)

    def export(self):
        data = self.repository.get_all()
        with open("result_files/result.json", "w", encoding="utf-8") as jp:
            js = json.dumps(
                data, default=lambda o: o.__dict__, sort_keys=True, indent=4
            )
            jp.write(js)

    def __save__(self, uf: str, table: dict):
        for row in table:
            cep_range = CepRangeModel(
                uf, row.get("Localidade"), row.get("Faixa de CEP")
            )
            self.repository.insert(cep_range)

    def __get_list_dict__(self, path: str) -> list:
        data = self.scrapy.get_outer_html_element(path)
        return self.handler.parse_table_to_dict(data)
