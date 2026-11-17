# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/impl/lobby/event_welcome_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from PlayerEvents import g_playerEvents as g_playerEvents
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.impl.gen import R as R
from gui.impl.pub import WindowImpl as WindowImpl, ViewImpl as ViewImpl
from helpers.time_utils import getTimestampFromUTC as getTimestampFromUTC
from story_mode.account_settings import setWelcomeScreenSeen as setWelcomeScreenSeen
from story_mode.gui.impl.gen.view_models.views.lobby.event_welcome_view_model import EventWelcomeViewModel as EventWelcomeViewModel
from story_mode_common.configs.story_mode_settings import settingsSchema as settingsSchema
from story_mode.uilogging.story_mode.loggers import EventWelcomeViewLogger as EventWelcomeViewLogger

class EventWelcomeView(ViewImpl):
    __slots__: tuple
    layoutID: Any
    _uiLogger: Any
    def __init__(self, layoutID=None):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def __fillViewModel(self):
        ...
    def __onClose(self):
        ...
    def __onDisconnected(self):
        ...

class EventWelcomeWindow(WindowImpl):
    def __init__(self, layoutID):
        ...
