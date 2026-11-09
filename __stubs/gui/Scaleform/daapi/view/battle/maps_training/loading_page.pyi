# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/maps_training/loading_page.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.meta.MapsTrainingBattleLoadingMeta import MapsTrainingBattleLoadingMeta as MapsTrainingBattleLoadingMeta
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES as BATTLE_VIEW_ALIASES
from gui.battle_control.arena_info.interfaces import IArenaLoadController as IArenaLoadController
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, g_eventBus as g_eventBus
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_HTML_TEMPLATE_PATH = 'html_templates:mapsTraining/loadingScreen'

class MapsTrainingLoadingPage(MapsTrainingBattleLoadingMeta, IArenaLoadController):
    sessionProvider: Any
    def _populate(self):
        ...
    @staticmethod
    def __getPageConfig(pageNum):
        ...
    def _dispose(self):
        ...
    def updateSpaceLoadProgress(self, progress):
        ...
    def __handleBattleLoading(self, event):
        ...
