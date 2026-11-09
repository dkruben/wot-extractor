# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/ui/util.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import viewitems as viewitems
from past.builtins import basestring as basestring
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import NEW_LOBBY_TAB_COUNTER as NEW_LOBBY_TAB_COUNTER
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as ACHIEVEMENT_BLOCK
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.vehicle_preview.items_kit_helper import lookupItem as lookupItem, showItemTooltip as showItemTooltip, getCDFromId as getCDFromId, canInstallStyle as canInstallStyle, showAwardsTooltip as showAwardsTooltip
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TC
from gui.Scaleform.daapi.view.lobby.header import battle_selector_items as battle_selector_items
from gui.impl.lobby.common.lobby_header_utils import HEADER_BUTTONS_COUNTERS_CHANGED_EVENT as HEADER_BUTTONS_COUNTERS_CHANGED_EVENT
from gui.server_events.bonuses import getNonQuestBonuses as getNonQuestBonuses
from gui.shared import g_eventBus as g_eventBus
from gui.shared.events import HasCtxEvent as HasCtxEvent
from gui.shared.gui_items.dossier import dumpDossier as dumpDossier
from gui.shared.gui_items.dossier.achievements.abstract import isRareAchievement as isRareAchievement
from gui.shared.utils import showInvitationInWindowsBar as showInvitationInWindowsBar
from gui.shared.event_dispatcher import runSalesChain as runSalesChain
from gui.shared.view_helpers import UsersInfoHelper as UsersInfoHelper
from gui.shared.utils.functions import makeTooltip as makeTooltip
from helpers import time_utils as time_utils
from helpers import dependency as dependency
from messenger.storage import UsersStorage as UsersStorage, MessengerStorageDescriptor as MessengerStorageDescriptor
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.game_control import IExternalLinksController as IExternalLinksController
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.web import IWebController as IWebController
from web.web_client_api import w2c as w2c, W2CSchema as W2CSchema, Field as Field, WebCommandException as WebCommandException
from web.web_client_api.common import ItemPackType as ItemPackType, ItemPackEntry as ItemPackEntry, SPA_ID_TYPES as SPA_ID_TYPES
from gui.wgcg.utils.contexts import SPAAccountAttributeCtx as SPAAccountAttributeCtx, PlatformFetchProductListCtx as PlatformFetchProductListCtx
from web.web_client_api.ui.vehicle import _VehicleCustomizationPreviewSchema as _VehicleCustomizationPreviewSchema
from items import makeIntCompactDescrByID as makeIntCompactDescrByID, parseIntCompactDescr as parseIntCompactDescr
from items.components.crew_books_constants import CrewBookCacheType as CrewBookCacheType
from gui.Scaleform.framework.entities.abstract.ToolTipMgrMeta import ToolTipMgrMeta as ToolTipMgrMeta
_COUNTER_IDS_MAP: dict

class _SetCounterSchema(W2CSchema):
    id: Any
    value: Any

class _GetCountersSchema(W2CSchema):
    id_list: Any

class _RunTriggerChainSchema(W2CSchema):
    trigger_chain_id: Any

class _ShowToolTipSchema(W2CSchema):
    tooltipType: Any
    itemId: Any
    blockId: Any

class _ShowCustomTooltipSchema(W2CSchema):
    header: Any
    body: Any

class _ShowSimpleTooltipSchema(W2CSchema):
    body: Any

class _ShowItemTooltipSchema(W2CSchema):
    id: Any
    type: Any
    count: Any
    extra: Any

class _ShowAwardsTooltipSchema(W2CSchema):
    type: Any
    data: Any

class _ChatAvailabilitySchema(W2CSchema):
    receiver_id: Any

class _AccountAttribute(W2CSchema):
    attr_prefix: Any

class _PlatformProductListSchema(W2CSchema):
    storefront: Any
    wgid: Any
    language: Any
    additional_data: Any
    country: Any
    response_fields: Any
    response_fields_profile: Any
    category: Any
    product_codes: Any

class _SelectBattleTypeSchema(W2CSchema):
    battle_type: Any

class _UrlInfoSchema(W2CSchema):
    url: Any

class _ShowAdditionalRewardsTooltipSchema(W2CSchema):
    rewards: Any
    x: Any
    y: Any

class _ShowCollectionItemTooltipSchema(W2CSchema):
    cd: Any
    x: Any
    y: Any

class UtilWebApiMixin(object):
    itemsCache: Any
    goodiesCache: Any
    _webCtrl: Any
    _lnkCtrl: Any
    usersStorage: Any
    __usersInfoHelper: Any
    def __init__(self):
        ...
    # decorador original: @w2c(...)
    def setCounterState(self, cmd):
        ...
    # decorador original: @w2c(...)
    def getCountersInfo(self, cmd):
        ...
    # decorador original: @w2c(...)
    def blinkTaskbar(self, _):
        ...
    # decorador original: @w2c(...)
    def runTriggerChain(self, cmd):
        ...
    # decorador original: @w2c(...)
    def showTooltip(self, cmd):
        ...
    # decorador original: @w2c(...)
    def showItemTooltip(self, cmd):
        ...
    # decorador original: @w2c(...)
    def showAwardsTooltip(self, cmd):
        ...
    # decorador original: @w2c(...)
    def showCustomTooltip(self, cmd):
        ...
    # decorador original: @w2c(...)
    def showSimpleTooltip(self, cmd):
        ...
    # decorador original: @w2c(...)
    def hideToolTip(self, _):
        ...
    # decorador original: @w2c(...)
    def hideWulfToolTip(self, _):
        ...
    def _hideWulfToolTip(self):
        ...
    # decorador original: @w2c(...)
    def showAdditionalRewardsTooltip(self, cmd):
        ...
    # decorador original: @w2c(...)
    def showCollectionItemTooltip(self, cmd):
        ...
    # decorador original: @w2c(...)
    def getCurrentLocalServerTimestamp(self, _):
        ...
    # decorador original: @w2c(...)
    def handleFetchProductList(self, cmd):
        ...
    # decorador original: @w2c(...)
    def handleGetAccountAttributeByPrefix(self, cmd):
        ...
    # decorador original: @w2c(...)
    def checkIfChatAvailable(self, cmd):
        ...
    # decorador original: @w2c(...)
    def canStyleBeInstalled(self, cmd):
        ...
    def _getTooltipMgr(self):
        ...
    @staticmethod
    def __getErrorResponse(data, defaultError=''):
        ...
    # decorador original: @w2c(...)
    def selectBattleType(self, cmd):
        ...
    # decorador original: @w2c(...)
    def getUrlInfo(self, cmd):
        ...

def _itemTypeValidator(itemType, _=None):
    ...
def _counterIdValidator(counterId, _=None):
    ...
def _counterIdsValidator(idList, _=None):
    ...
