# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/Scaleform/daapi/view/lobby/battle_queue.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin as FunAssetPacksMixin, FunSubModesWatcher as FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasDesiredSubMode as hasDesiredSubMode
from gui.Scaleform.daapi.view.lobby.battle_queue.battle_queue import RandomQueueProvider as RandomQueueProvider
from gui.impl import backport as backport

class FunRandomQueueProvider(RandomQueueProvider, FunAssetPacksMixin, FunSubModesWatcher):
    _needAdditionalInfo: Any
    def getIconPath(self, iconLabel):
        ...
    def getTitle(self, guiType):
        ...
    def processQueueInfo(self, qInfo):
        ...
    # decorador original: @hasDesiredSubMode(...)
    def needAdditionalInfo(self):
        ...
    # decorador original: @hasDesiredSubMode(...)
    def _doRequestQueueInfo(self, currPlayer):
        ...
    def _getRequestQueueInfoParams(self):
        ...
    # decorador original: @hasDesiredSubMode(...)
    def __getTitle(self):
        ...
