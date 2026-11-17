# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/presenters/utils.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import namedtuple as namedtuple, OrderedDict as OrderedDict
from functools import partial as partial
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.header import battle_selector_items as battle_selector_items
from gui.clans.clan_helpers import isStrongholdsEnabled as isStrongholdsEnabled
from gui.impl.gen.view_models.views.lobby.hangar.main_menu_model import MainMenuModel as MainMenuModel
from gui.impl.gen.view_models.views.lobby.hangar.menu_item_model import MenuItemModel as MenuItemModel
from gui.server_events.events_dispatcher import showMissions as showMissions
from gui.shared.event_dispatcher import showShop as showShop, showStorage as showStorage, showBarracks as showBarracks, showViewByAlias as showViewByAlias, showTechTree as showTechTree, showModeSelectorWindow as showModeSelectorWindow, showPersonalMissionCampaignSelectorWindow as showPersonalMissionCampaignSelectorWindow, showServiceRecordWindow as showServiceRecordWindow
from gui.shared.system_factory import registerMenuItems as registerMenuItems, collectMenuItems as collectMenuItems
from gui.tournament.tournament_helpers import showTournaments as showTournaments, isTournamentEnabled as isTournamentEnabled
from helpers import dependency as dependency
from items import vehicles as vehicles
from items.components.c11n_constants import CustomizationType as CustomizationType
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from shared_utils import findFirst as findFirst
GUINode: Any
MenuItemEntry: Any
SHARED_MENU_ITEMS: Any
SHOP_MENU_ITEM: tuple
STORAGE_MENU_ITEM: tuple
MISSIONS_MENU_ITEM: tuple
PERSONAL_MISSIONS_MENU_ITEM: tuple
ACHIEVEMENTS_MENU_ITEM: tuple
TECHTREE_MENU_ITEM: tuple
BARRACKS_MENU_ITEM: tuple
TOURNAMENT_MENU_ITEM: tuple
CLANS_MENU_ITEM: tuple
RANDOM_MENU_ITEMS: Any

# decorador original: @dependency.replace_none_kwargs(...)
def isPersonalMissionsEnabled(lobbyContext=None):
    ...
def getSharedMenuItems():
    ...
def getMenuItems():
    ...
def fillMenuItems(model, menuData=None):
    ...
def fillMenuSharedItems(model, menuData=None):
    ...
def navigateTo(args):
    ...
def take3DStyles(customizationSerivce):
    ...
