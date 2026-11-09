# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/battle/battle_page/full_stats/personal_reserves_tab_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import BigWorld as BigWorld
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.impl.common.personal_reserves.personal_reserves_shared_constants import PERSONAL_RESOURCE_ORDER as PERSONAL_RESOURCE_ORDER
from gui.impl.common.personal_reserves.personal_reserves_shared_model_utils import getPersonalBoosterModelDataByResourceType as getPersonalBoosterModelDataByResourceType, addPersonalBoostersGroup as addPersonalBoostersGroup, addEventGroup as addEventGroup
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.battle.battle_page.personal_reserves_tab_view_model import PersonalReservesTabViewModel as PersonalReservesTabViewModel, TabAlias as TabAlias
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.personal_reserves.personal_reserves_utils import generatePersonalReserveTick as generatePersonalReserveTick
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from gui.shared.utils.scheduled_notifications import Notifiable as Notifiable, PeriodicNotifier as PeriodicNotifier
from gui.battle_control.battle_constants import TabsAliases as TabsAliases
from helpers import dependency as dependency
from skeletons.gui.goodies import IBoostersStateProvider as IBoostersStateProvider
from frameworks.wulf import ViewModel as ViewModel
from typing import List as List, Dict as Dict
from frameworks.wulf import Array as Array
from frameworks.wulf.view.view import View as View
from frameworks.wulf.view.view_event import ViewEvent as ViewEvent
from gui.goodies.booster_state_provider import BoosterStateProvider as BoosterStateProvider
from gui.impl.gen.view_models.common.personal_reserves.reserves_group_model import ReservesGroupModel as ReservesGroupModel
from gui.impl.common.personal_reserves.personal_reserves_shared_model_utils import BoosterModelData as BoosterModelData
_logger: Any

class PersonalReservesTabView(ViewImpl):
    __slots__: tuple
    _boostersStateProvider: Any
    _notificatorManager: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def handleTabChange(self, tabAlias):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def activatePersonalReserve(self, boosterId):
        ...
    # decorador original: @args2params(...)
    def onBoosterActivate(self, boosterId):
        ...
    def _update(self):
        ...
    def fillViewModel(self):
        ...
    def _timeTillNextPersonalReserveTick(self):
        ...
