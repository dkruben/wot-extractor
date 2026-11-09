# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/anomalies_watcher_mixin.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class AnomaliesWatcherMixin(object):
    sessionProvider: Any
    needToShow: Any
    __isDisplayAllowed: Any
    def __init__(self, *args, **kwargs):
        ...
    def updateVisibility(self):
        ...
    @property
    def isDisplayAllowed(self):
        ...
    @property
    def hwBattleGuiCtrl(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __onChangeAnomaliesViewVisibility(self, isVisible):
        ...
