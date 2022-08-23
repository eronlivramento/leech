from src.model.cep_range import CepRangeModel


class CepRangeRepositoryMock:
    def __init__(self) -> None:
        self.model_list = []

    def insert(self, model: CepRangeModel):
        self.model_list.append(model)

    def get_all(self) -> list:
        return self.model_list
