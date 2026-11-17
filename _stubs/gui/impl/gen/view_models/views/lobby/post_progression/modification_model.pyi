# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/post_progression/modification_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from gui.impl.gen.view_models.common.price_model import PriceModel as PriceModel
from gui.impl.gen.view_models.views.lobby.post_progression.base_modification_model import BaseModificationModel as BaseModificationModel

class RoleCategory(Enum):
    FIREPOWER = 'firepower'
    SURVIVABILITY = 'survivability'
    MOBILITY = 'mobility'
    STEALTH = 'stealth'
    NONE = 'none'

class ModificationModel(BaseModificationModel):
    __slots__: tuple
    def __init__(self, properties=6, commands=0):
        ...
    @property
    def price(self):
        ...
    @staticmethod
    def getPriceType():
        ...
    def getRoleCategory(self):
        ...
    def setRoleCategory(self, value):
        ...
    def _initialize(self):
        ...
