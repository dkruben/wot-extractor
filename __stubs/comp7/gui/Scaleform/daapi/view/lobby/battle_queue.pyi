# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/Scaleform/daapi/view/lobby/battle_queue.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import constants as constants
from comp7.gui.impl.gen.view_models.views.lobby.enums import SeasonName as SeasonName
from comp7.gui.impl.lobby.comp7_helpers import comp7_shared as comp7_shared, comp7_i18n_helpers as comp7_i18n_helpers
from comp7_core.gui.impl.lobby.comp7_core_helpers import comp7_core_model_helpers as comp7_core_model_helpers
from gui.Scaleform.daapi.view.lobby.battle_queue.battle_queue import RandomQueueProvider as RandomQueueProvider
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7Controller as IComp7Controller

class Comp7QueueProvider(RandomQueueProvider):
    __comp7Controller: Any
    def processQueueInfo(self, qInfo):
        ...
    def getLayoutStr(self):
        ...
    def getIconPath(self, iconLabel):
        ...
    def getTankInfoLabel(self):
        ...
    def getTankIcon(self, vehicle):
        ...
    def getTankName(self, vehicle):
        ...
    def needAdditionalInfo(self):
        ...
    def additionalInfo(self):
        ...
    def __getRankData(self, rankName, playersCount, isHighlight):
        ...
