# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/game_mode_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import IntEnum as IntEnum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.battle_royale_conditions_model import BattleRoyaleConditionsModel as BattleRoyaleConditionsModel
from gui.impl.gen.view_models.views.lobby.battle_pass.game_mode_rows_model import GameModeRowsModel as GameModeRowsModel

class ArenaBonusType(IntEnum):
    REGULAR = 1
    RANKED = 22
    BATTLE_ROYALE_SOLO = 29
    EPIC_BATTLE = 27
    COMP7 = 43
    COMP7_LIGHT = 49

class PointsCardType(IntEnum):
    LIMIT = 0
    DAILY = 1

class GameModeModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=5, commands=0):
        ...
    @property
    def battleRoyaleCondtions(self):
        ...
    @staticmethod
    def getBattleRoyaleCondtionsType():
        ...
    def getArenaBonusType(self):
        ...
    def setArenaBonusType(self, value):
        ...
    def getConditions(self):
        ...
    def setConditions(self, value):
        ...
    @staticmethod
    def getConditionsType():
        ...
    def getVehicles(self):
        ...
    def setVehicles(self, value):
        ...
    @staticmethod
    def getVehiclesType():
        ...
    def getCards(self):
        ...
    def setCards(self, value):
        ...
    @staticmethod
    def getCardsType():
        ...
    def _initialize(self):
        ...
