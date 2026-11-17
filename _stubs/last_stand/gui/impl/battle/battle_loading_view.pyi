# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/battle/battle_loading_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer
from gui.battle_control.arena_info.interfaces import IArenaLoadController as IArenaLoadController
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from last_stand.gui.impl.gen.view_models.views.battle.event_loading_view_model import EventLoadingViewModel as EventLoadingViewModel
from helpers import dependency as dependency
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from gui.impl.gen import R as R
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_logger: Any

class BattleLoadingView(ViewImpl, IArenaLoadController):
    sessionProvider: Any
    def __init__(self, layoutID):
        ...
    def updateSpaceLoadProgress(self, progress):
        ...
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateProgress(self, progress, model=None):
        ...

class BattleLoadingWindow(WindowImpl):
    __slots__: tuple
    sessionProvider: Any
    def __init__(self, parent=None):
        ...
