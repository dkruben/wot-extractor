# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/impl/gen/view_models/views/lobby/battle_result_stat_tooltip_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from story_mode.gui.impl.gen.view_models.views.lobby.detailed_stat_model import DetailedStatModel as DetailedStatModel

class StatEnum(Enum):
    MISSIONS = 'missions'
    ASSIST = 'assist'
    KILLS = 'kills'
    DAMAGE = 'damage'
    ARMOR_USE = 'armorUse'

class BattleResultStatTooltipModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=3, commands=0):
        ...
    def getStat(self):
        ...
    def setStat(self, value):
        ...
    def getDetailedStats(self):
        ...
    def setDetailedStats(self, value):
        ...
    @staticmethod
    def getDetailedStatsType():
        ...
    def getInfoList(self):
        ...
    def setInfoList(self, value):
        ...
    @staticmethod
    def getInfoListType():
        ...
    def _initialize(self):
        ...
