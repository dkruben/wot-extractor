# wot-extractor: STUB (.pyi) gerado a partir de sources/res/advent_calendar/scripts/client/advent_calendar/gui/impl/lobby/feature/intro_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from account_helpers.AccountSettings import AdventCalendar as AdventCalendar
from advent_calendar.gui.impl.gen.view_models.views.lobby.intro_screen_model import IntroScreenModel as IntroScreenModel
from advent_calendar.gui.impl.lobby.feature.advent_helper import isAdventAnimationEnabled as isAdventAnimationEnabled, setAdventCalendarSetting as setAdventCalendarSetting
from advent_calendar.gui.shared import events as events
from advent_calendar.skeletons import IAdventCalendarController as IAdventCalendarController
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow as LobbyWindow
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from helpers import dependency as dependency
_logger: Any

class AdventCalendarIntroView(ViewImpl):
    __adventController: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    @staticmethod
    def __onCloseAnimationStarted():
        ...
    def __onClose(self):
        ...

class AdventCalendarIntroWindow(LobbyWindow):
    def __init__(self, parent=None, **kwargs):
        ...
