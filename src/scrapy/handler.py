from bs4 import BeautifulSoup
import pandas


class Handler:
    def parse_table_to_dict(self, content: str) -> list:
        soup = BeautifulSoup(content, "html.parser")
        table = soup.find(name="table")
        df_full = pandas.read_html(str(table))[0]
        df = df_full[["Localidade", "Faixa de CEP"]]
        df.columns = ["Localidade", "Faixa de CEP"]
        return df.to_dict("records")
