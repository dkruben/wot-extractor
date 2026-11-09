# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/dog_tags/customization_confirm_dialog_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.dog_tags.dt_dog_tag import DtDogTag as DtDogTag

class CustomizationConfirmDialogModel(ViewModel):
    __slots__: tuple
    onClose: Any
    onDiscard: Any
    onConfirm: Any
    def __init__(self, properties=1, commands=3):
        ...
    @property
    def equippedDogTag(self):
        ...
    @staticmethod
    def getEquippedDogTagType():
        ...
    def _initialize(self):
        ...
