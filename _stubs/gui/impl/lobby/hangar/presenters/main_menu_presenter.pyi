# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/presenters/main_menu_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from constants import GF_RES_PROTOCOL as GF_RES_PROTOCOL, PremiumConfigs as PremiumConfigs, DAILY_QUESTS_CONFIG as DAILY_QUESTS_CONFIG
from PlayerEvents import g_playerEvents as g_playerEvents
from frameworks.wulf import ViewStatus as ViewStatus
from gui.clans.clan_cache import g_clanCache as g_clanCache
from gui.impl.gen.view_models.views.lobby.hangar.main_menu_model import MainMenuModel as MainMenuModel
from gui.impl.lobby.hangar.presenters.utils import fillMenuItems as fillMenuItems
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.shared.image_helper import getTextureLinkByID as getTextureLinkByID
from gui.shared.view_helpers import ClanEmblemsHelper as ClanEmblemsHelper
from helpers import dependency as dependency
from personal_missions import PM_SWITCHES as PM_SWITCHES
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.techtree_events import ITechTreeEventsListener as ITechTreeEventsListener
from collections import OrderedDict as OrderedDict
_logger: Any

# base nao representavel no stub: ViewComponent[...]
class MainMenuPresenter(ClanEmblemsHelper, IGlobalListener):
    __techTreeEventsListener: Any
    __lobbyContext: Any
    __menuItems: Any
    __clanIconID: Any
    def __init__(self, menuItems):
        ...
    @property
    def viewModel(self):
        ...
    def onClanEmblem32x32Received(self, clanDbID, emblem):
        ...
    def onPrbEntitySwitched(self, _=None):
        ...
    def _getEvents(self):
        ...
    def _getCallbacks(self):
        ...
    def _navigateTo(self, args):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __updateModel(self):
        ...
    def __requestClanEmblem(self, *_):
        ...
    def __removeClanIconFromMemory(self):
        ...
    def __clansMenuItemExists(self):
        ...
    def __onServerSettingsChanged(self, diff=None):
        ...
