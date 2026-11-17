# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/common/toggle_button_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from gui.impl.gen.view_models.views.lobby.crew.common.button_model import ButtonModel as ButtonModel

class ToggleState(Enum):
    ON = 'on'
    OFF = 'off'
    DISABLED = 'disabled'
    HIDDEN = 'hidden'

class ToggleButtonModel(ButtonModel):
    __slots__: tuple
    def __init__(self, properties=3, commands=0):
        ...
    def getState(self):
        ...
    def setState(self, value):
        ...
    def getIsDisabled(self):
        ...
    def setIsDisabled(self, value):
        ...
    def _initialize(self):
        ...
