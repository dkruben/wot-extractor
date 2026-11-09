# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/battle_royale/battle_results/player_battle_type_status_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.common.user_name_model import UserNameModel as UserNameModel

class BattleType(Enum):
    SOLO = 'solo'
    RANDOMPLATOON = 'randomPlatoon'
    PLATOON = 'platoon'

class PlayerBattleTypeStatusModel(ViewModel):
    __slots__: tuple
    onInviteToPlatoon: Any
    def __init__(self, properties=3, commands=1):
        ...
    @property
    def user(self):
        ...
    @staticmethod
    def getUserType():
        ...
    def getBattleType(self):
        ...
    def setBattleType(self, value):
        ...
    def getIsPlatoonWindowOpen(self):
        ...
    def setIsPlatoonWindowOpen(self, value):
        ...
    def _initialize(self):
        ...
