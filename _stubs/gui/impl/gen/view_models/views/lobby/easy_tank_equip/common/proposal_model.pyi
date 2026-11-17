# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/easy_tank_equip/common/proposal_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
T: Any

class ProposalDisableReason(Enum):
    NONE = 'none'
    NOT_FORMED = 'notFormed'
    BUILT_IN_STYLE = 'builtInStyle'

class ProposalType(Enum):
    NONE = 'none'
    CREW = 'crew'
    OPT_DEVICES = 'optDevices'
    SHELLS = 'shells'
    CONSUMABLES = 'consumables'
    STYLES = 'styles'

# base nao representavel no stub: typing.Generic[...]
class ProposalModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=4, commands=0):
        ...
    def getSelected(self):
        ...
    def setSelected(self, value):
        ...
    def getDisableReason(self):
        ...
    def setDisableReason(self, value):
        ...
    def getPresetIndex(self):
        ...
    def setPresetIndex(self, value):
        ...
    def getPresets(self):
        ...
    def setPresets(self, value):
        ...
    @staticmethod
    def getPresetsType():
        ...
    def _initialize(self):
        ...
