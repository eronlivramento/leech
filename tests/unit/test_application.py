
import os
from src.app.application import Application
from tests.mock.cep_range_repository_mock import CepRangeRepositoryMock


class TestApplication:

    def test_run(self):
        ROOT_DIR = os.path.dirname(os.path.abspath("page_mock.html"))
        url = f"file://{ROOT_DIR}/tests/mock/page_mock.html"
        repository = CepRangeRepositoryMock()
        input_fields = {
            'field_list': '*//select[@name="UF"]',
            'select_option': '*//select[@name="UF"]',
            'submit_form': '*//div[@class="btnform"]//input',
            'data_capture': '*//table[2]',
            'has_navegation': '*//a[text()="[ Próxima ]"]',
            'navegation': '*//a[text()="[ Próxima ]"]',
            'data_capture_navegation': '*//table',
            'back_form': '*//a[text()="[ Nova Consulta ]"]'
        }
        app = Application(url, repository, input_fields)
        app.run()
        assert len(app.repository.get_all()) == 4
