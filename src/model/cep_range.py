class CepRangeModel:
    def __init__(self, state: str, location: str, range: str, id: int = 0) -> None:
        self.id = id
        self.state = state
        self.location = location
        self.range = range
        pass
