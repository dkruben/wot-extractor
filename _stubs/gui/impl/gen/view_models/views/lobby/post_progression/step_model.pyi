# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/post_progression/step_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from gui.impl.gen.view_models.views.lobby.post_progression.base_step_model import BaseStepModel as BaseStepModel
from gui.impl.gen.view_models.views.lobby.post_progression.restrictions_model import RestrictionsModel as RestrictionsModel

class ActionState(Enum):
    PERSISTENT = 'persistent'
    SELECTABLE = 'selectable'
    CHANGEABLE = 'changeable'

class StepState(Enum):
    RESTRICTED = 'restricted'
    UNAVAILABLELOCKED = 'unavailableLocked'
    AVAILABLEPURCHASE = 'availablePurchase'
    RECEIVED = 'received'

class StepModel(BaseStepModel):
    __slots__: tuple
    def __init__(self, properties=6, commands=0):
        ...
    @property
    def restrictions(self):
        ...
    @staticmethod
    def getRestrictionsType():
        ...
    def getIsDisabled(self):
        ...
    def setIsDisabled(self, value):
        ...
    def getActionState(self):
        ...
    def setActionState(self, value):
        ...
    def getStepState(self):
        ...
    def setStepState(self, value):
        ...
    def _initialize(self):
        ...
