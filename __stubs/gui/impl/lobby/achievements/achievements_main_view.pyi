# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/achievements/achievements_main_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from functools import partial as partial
import typing as typing
from collections import namedtuple as namedtuple
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.shared import events as events, g_eventBus as g_eventBus
from gui.shared.event_bus import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.impl.gen.view_models.views.lobby.achievements.views.achievements_main_view_model import AchievementsViews as AchievementsViews, AchievementsMainViewModel as AchievementsMainViewModel
from frameworks.wulf.view.submodel_presenter import SubModelPresenter as SubModelPresenter
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import uniprof as uniprof
from typing import Dict as Dict
_SubModelInfo: Any
AchievementsViewCtx: Any

class BaseAchievementView(ViewImpl):
    __slots__: tuple
    _ctx: Any
    def __init__(self, ctx, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _onClose(self):
        ...
    @property
    def currentPresenter(self):
        ...
    def _finalize(self):
        ...

class AchievementMainView(BaseAchievementView):
    __slots__: tuple
    _ctx: Any
    __contentPresentersMap: Any
    __regionName: Any
    def __init__(self, ctx, *args, **kwargs):
        ...
    @property
    def currentPresenter(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def createToolTip(self, event):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getListeners(self):
        ...
    def _onClose(self):
        ...
    def _finalize(self):
        ...
    def __registerSubModels(self):
        ...
    def __switchSubViewEventHandler(self, event):
        ...
    def __switchSubView(self, ctx):
        ...

class _PresentersMap(object):
    __presentersCache: Any
    __mainView: Any
    __userId: Any
    __loadersMap: Any
    def __init__(self, mainView, userId):
        ...
    def itervalues(self):
        ...
    def clear(self):
        ...
    def __getitem__(self, item):
        ...
    def __tryToLoadPresenter(self, key):
        ...
    def __loadSummary(self):
        ...
    def __loadAchievements(self):
        ...
    @staticmethod
    def __makeSubModel(viewAlias, loader, customPredicate=None):
        ...
