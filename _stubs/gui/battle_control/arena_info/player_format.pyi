# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/arena_info/player_format.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
_PLAYER_FULL_NAME_FORMATS: dict
PlayerFormatResult: Any

class _FORMAT_MASK(object):
    NONE = 0
    VEHICLE = 1
    CLAN = 16
    REGION = 256
    VEH_CLAN: Any
    VEH_REGION: Any
    REG_CLAN: Any
    ALL: Any

class PlayerFullNameFormatter(object):
    __isVehicleShortNameShown: Any
    __isClanShown: Any
    __isRegionShown: Any
    def __init__(self):
        ...
    @classmethod
    def create(cls, isVehicleShortNameShown=True, isClanShown=True, isRegionShown=True):
        ...
    def setVehicleShortNameShown(self, flag):
        ...
    def setClanShown(self, flag):
        ...
    def setRegionShown(self, flag):
        ...
    def format(self, vInfoVO, playerName=None):
        ...
    @staticmethod
    def _normalizePlayerName(name):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def getRegionCode(accountDBID, lobbyContext=None):
    ...
