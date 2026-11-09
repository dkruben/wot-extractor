# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/gf_notifications/crew_reward_notification.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.gen.view_models.views.lobby.crew.tankman_model import TankmanKind as TankmanKind
from gui.impl.lobby.crew.filter import FilterState as FilterState
from gui.impl.lobby.crew.filter.data_providers import RecruitsDataProvider as RecruitsDataProvider
from gui.impl.lobby.crew.filter.state import Persistor as Persistor
from gui.impl.lobby.gf_notifications.notification_base import NotificationBase as NotificationBase
from halloween.gui.impl.gen.view_models.views.lobby.notifications.crew_reward_notification_model import CrewRewardNotificationModel as CrewRewardNotificationModel
from gui.shared.event_dispatcher import showBarracks as showBarracks
from halloween.skeletons.halloween_twitch_con_controller import IHalloweenTwitchConController as IHalloweenTwitchConController
from helpers import dependency as dependency
from gui.server_events.recruit_helper import getRecruitInfo as getRecruitInfo
from shared_utils import first as first

class CrewRewardNotification(NotificationBase):
    _hwTwitchConCtrl: Any
    _filterState: Any
    _recruitsDataProvider: Any
    def __init__(self, resId, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    @property
    def viewModel(self):
        ...
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def _update(self):
        ...
    def _onRecruit(self):
        ...
