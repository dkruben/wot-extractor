# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/tooltips/banner_tooltip_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_royale_event_model import BattleRoyaleEventModel as BattleRoyaleEventModel

class PerformanceRisk(Enum):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

class BannerTooltipViewModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=4, commands=0):
        ...
    @property
    def eventInfo(self):
        ...
    @staticmethod
    def getEventInfoType():
        ...
    def getTime(self):
        ...
    def setTime(self, value):
        ...
    def getModeState(self):
        ...
    def setModeState(self, value):
        ...
    def getPerformanceRisk(self):
        ...
    def setPerformanceRisk(self, value):
        ...
    def _initialize(self):
        ...
