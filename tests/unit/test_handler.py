from src.scrapy.handler import Handler
from tests.mock.table_mock import get_table_mock


class TestHandler:
    def test_parse_table_to_dict(self):
        table = get_table_mock()
        hander = Handler()
        result = hander.parse_table_to_dict(table)
        instance = list
        print( isinstance(result, instance))
