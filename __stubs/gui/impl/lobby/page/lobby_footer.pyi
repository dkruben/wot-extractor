# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/page/lobby_footer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as t
from frameworks.wulf import WindowLayer as WindowLayer
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.page.footer.default_model import DefaultModel as DefaultModel
from gui.impl.lobby.page.chats_presenter import ChatsPresenter as ChatsPresenter
from gui.impl.lobby.page.contacts_list_presenter import ContactsListPresenter as ContactsListPresenter
from gui.impl.lobby.page.notifications_center_presenter import NotificationsCenterPresenter as NotificationsCenterPresenter
from gui.impl.lobby.page.platoon_presenter import PlatoonPresenter as PlatoonPresenter
from gui.impl.lobby.page.referral_program_presenter import ReferralProgramPresenter as ReferralProgramPresenter
from gui.impl.lobby.page.server_info_presenter import ServerInfoPresenter as ServerInfoPresenter
from gui.impl.lobby.page.session_stats_presenter import SessionStatsPresenter as SessionStatsPresenter
from gui.impl.lobby.page.vehicle_compare_presenter import VehicleComparePresenter as VehicleComparePresenter
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.shared.event_dispatcher import showLobbyMenu as showLobbyMenu
from helpers import dependency as dependency
from skeletons.gui.game_control import IPlatoonController as IPlatoonController
from Event import Event as Event
_logger: Any

# base nao representavel no stub: ViewComponent[...]
class LobbyFooter(IGlobalListener):
    __platoonCtrl: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def setOldStyleViewFlag(self, value):
        ...
    def _initChildren(self):
        ...
    def _getEvents(self):
        ...
    def __showLobbyMenu(self):
        ...
    def _getPopOverLayer(self):
        ...
