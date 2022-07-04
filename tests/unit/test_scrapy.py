import os
from src.scrapy.scrapy import Scrapy

ROOT_DIR = os.path.dirname(os.path.abspath("page_mock.html"))
url = f"file://{ROOT_DIR}/tests/mock/page_mock.html"
scrapy = Scrapy(url)
scrapy.start()


class TestScrapy:

    def test_get_element_text(self):
        assert scrapy.get_element_text("*//p") == "Mock Text"

    def test_check_if_exist_not_found(self):
        assert scrapy.check_if_exist("html/a") is False

    def test_check_if_exist_found(self):
        assert scrapy.check_if_exist("*//p")

    def test_get_outer_html_element(self):
        assert scrapy.get_outer_html_element("*//p") == "<p>Mock Text</p>"

    def test_click_clicked(self):
        assert scrapy.click("*//a")

    def test_select_option(self):
        assert scrapy.select_option("*//select", "AC")
