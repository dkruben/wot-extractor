# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/items_cache.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from builtins import range as range
from Event import SafeEvent as SafeEvent
from debug_utils import LOG_DEBUG as LOG_DEBUG
from PlayerEvents import g_playerEvents as g_playerEvents
from gui.challenges.challenges_requester import ChallengesRequester as ChallengesRequester
from gui.server_events.events_helpers import isSuitableForPM as isSuitableForPM
from gui.pet_system.requester import PetRequesterRequester as PetRequesterRequester
from gui.shared.utils.requesters import DossierRequester as DossierRequester, GoodiesRequester as GoodiesRequester, InventoryRequester as InventoryRequester, ItemsRequester as ItemsRequester, RecycleBinRequester as RecycleBinRequester, ShopRequester as ShopRequester, StatsRequester as StatsRequester, TokensRequester as TokensRequester, VehicleRotationRequester as VehicleRotationRequester
from gui.shared.utils.requesters.anonymizer_requester import AnonymizerRequester as AnonymizerRequester
from gui.shared.utils.requesters.badges_requester import BadgesRequester as BadgesRequester
from gui.shared.utils.requesters.RankedRequester import RankedRequester as RankedRequester
from gui.shared.utils.requesters.BattleRoyaleRequester import BattleRoyaleRequester as BattleRoyaleRequester
from gui.shared.utils.requesters.EpicMetaGameRequester import EpicMetaGameRequester as EpicMetaGameRequester
from gui.shared.utils.requesters.battle_pass_requester import BattlePassRequester as BattlePassRequester
from gui.shared.utils.requesters.blueprints_requester import BlueprintsRequester as BlueprintsRequester
from gui.shared.utils.requesters.game_restrictions_requester import GameRestrictionsRequester as GameRestrictionsRequester
from gui.shared.utils.requesters.session_stats_requester import SessionStatsRequester as SessionStatsRequester
from gui.shared.utils.requesters.gift_system_requester import GiftSystemRequester as GiftSystemRequester
from gui.shared.utils.requesters.achievements20_requester import Achievements20Requester as Achievements20Requester
from gui.shared.compat_vehicles_cache import CompatVehiclesCache as CompatVehiclesCache
from helpers import dependency as dependency
from skeletons.festivity_factory import IFestivityFactory as IFestivityFactory
from skeletons.gui.shared import IItemsCache as IItemsCache
from soft_exception import SoftException as SoftException
from wg_async import wg_async as wg_async, wg_await as wg_await

class CACHE_SYNC_REASON(object):
    SHOW_GUI: Any
    CLIENT_UPDATE: Any
    SHOP_RESYNC: Any
    INVENTORY_RESYNC: Any
    DOSSIER_RESYNC: Any
    STATS_RESYNC: Any

class ItemsCache(IItemsCache):
    __isForPMSync: Any
    __needCommonSync: Any
    __items: Any
    __compatVehiclesCache: Any
    __waitForSync: Any
    __syncFailed: Any
    onSyncStarted: Any
    onSyncCompleted: Any
    onSyncFailed: Any
    onPMSyncCompleted: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    @property
    def waitForSync(self):
        ...
    @property
    def items(self):
        ...
    @property
    def compatVehiclesCache(self):
        ...
    # decorador original: @wg_async
    def update(self, updateReason, diff=None, notify=True):
        ...
    def clear(self):
        ...
    def request(self, callback=None):
        ...
    def onDisconnected(self):
        ...
    def _onResync(self, reason):
        ...
    def _onCenterIsLongDisconnected(self, isLongDisconnected):
        ...
    # decorador original: @wg_async
    def __invalidateData(self, updateReason, diff, notify=True):
        ...
    # decorador original: @wg_async
    def __invalidateFullData(self, updateReason, notify=True):
        ...
    def isSynced(self):
        ...
    def __pe_onStatsResync(self, *args):
        ...
    def __pe_onInventoryResync(self, *args):
        ...
    def __pe_onDossiersResync(self, *args):
        ...
