db = db.getSiblingDB('configs');

db.createCollection('sources');

db.sources.insertMany([{
    name: 'cep_range',
    url: 'https://www2.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm',
    input_element_path: '',
    env_db_host: 'GEO_HOST',
    env_db_port: 'GEO_PORT',
    env_db_name: 'GEO_DATABASE',
    env_db_schema: 'GEO_SCHEMA',
    env_input_table: 'CEP_INPUT_TABLE',
    input_fields: 'state, location, range',
    scrapy_path: {
                    'field_list': '*//select[@name="UF"]',
                    'select_option': '*//select[@name="UF"]',
                    'submit_form': '*//div[@class="btnform"]//input',
                    'data_capture': '*//table[2]',
                    'has_navegation': '*//a[text()="[ Próxima ]"]',
                    'navegation': '*//a[text()="[ Próxima ]"]',
                    'data_capture_navegation': '*//table',
                    'back_form': '*//a[text()="[ Nova Consulta ]"]'
                },
    env_db_user: 'GEO_USER',
    env_db_password: 'GEO_PASSWORD'

},
{
    name: 'dummy',
    url: 'https://dummy.com',
    input_element_path: '',
    env_db_host: 'DUMMY_DB_HOST',
    env_db_port: 'DUMMY_PORT',
    env_db_name: 'DUMMY_DATABASE',
    env_db_schema: 'DUMMY_SCHEMA',
    env_input_table: 'DUMMY_INPUT_TABLE',
    input_fields: {'dummy': 'dummy'},
    env_db_user: 'DUMMY_USER',
    env_db_password: 'DUMMY_PASSWORD'
}
]);