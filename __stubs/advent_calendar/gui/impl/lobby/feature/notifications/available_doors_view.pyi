# wot-extractor: STUB (.pyi) gerado a partir de sources/res/advent_calendar/scripts/client/advent_calendar/gui/impl/lobby/feature/notifications/available_doors_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers.AccountSettings import AdventCalendar as AdventCalendar
from advent_calendar.gui.impl.gen.view_models.views.lobby.notifications.available_doors_view_model import AvailableDoorsViewModel as AvailableDoorsViewModel, State as State
from advent_calendar.gui.impl.lobby.feature.advent_helper import setAdventCalendarSetting as setAdventCalendarSetting
from advent_calendar.gui.shared.event_dispatcher import showAdventCalendarMainWindow as showAdventCalendarMainWindow
from advent_calendar.skeletons import IAdventCalendarController as IAdventCalendarController
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.gf_notifications.notification_base import NotificationBase as NotificationBase
from helpers import dependency as dependency

class AvailableDoorsView(NotificationBase):
    _adventController: Any
    _DESCRIPTION_RESOURCE = ''
    _BACKGROUND_RESOURCE = ''
    def __init__(self, resId, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def rewardImagePath(self):
        ...
    def _getEvents(self):
        ...
    def _update(self):
        ...
    def _onClick(self):
        ...
