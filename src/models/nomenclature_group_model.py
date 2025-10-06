from src.core.abstract_model import abstract_model


class nomenclature_group_model(abstract_model):

    def __init__(self, name: str = None):
        super().__init__()
        if name is not None:
            self.name = name
