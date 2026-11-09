# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/game_control/ls_shop_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import Event as Event
from collections import namedtuple as namedtuple
from functools import cmp_to_key as cmp_to_key
from past.builtins import cmp as cmp
from future.utils import viewvalues as viewvalues, viewkeys as viewkeys, viewitems as viewitems
from adisp import adisp_async as adisp_async
from gui import SystemMessages as SystemMessages
from gui.shared.utils import decorators as decorators
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.server_events.bonuses import getNonQuestBonuses as getNonQuestBonuses, TokensBonus as TokensBonus
from last_stand.gui.shared.gui_items.processors.processors import BuyBundleProcessor as BuyBundleProcessor
from last_stand.skeletons.ls_controller import ILSController as ILSController
from last_stand.skeletons.ls_shop_controller import ILSShopController as ILSShopController
from last_stand_common.last_stand_constants import ShopSettings as ShopSettings, ProgressPointsSettings as ProgressPointsSettings
from helpers import dependency as dependency
from skeletons.gui.server_events import IEventsCache as IEventsCache
Price: Any

# base nao representavel no stub: namedtuple(...)
class Bundle:
    def getCtx(self):
        ...

class LSShopController(ILSShopController):
    eventsCache: Any
    lsCtrl: Any
    onShopSettingsUpdated: Any
    onBundlesUpdated: Any
    _bundles: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def keyBundles(self):
        ...
    def getBundleByID(self, bundleID):
        ...
    def getProgressPointsInBundle(self, bundleID):
        ...
    def isEnabled(self):
        ...
    def onLobbyStarted(self, ctx):
        ...
    # decorador original: @adisp_async
    # decorador original: @decorators.adisp_process(...)
    def purchaseBundle(self, bundleID, count, callback):
        ...
    def getPurchaseCount(self, bundleID):
        ...
    def checkIsEnoughBundles(self):
        ...
    def _initBundles(self):
        ...
    def _getBundleGroupID(self, bundleID):
        ...
    def _getBundleOrderInGroup(self, bundleID):
        ...
    def _getBundleDescrGroupKey(self, bundleID):
        ...
    def _getBundleLimit(self, bundleID):
        ...
    def _getBundleUrl(self, bundleID):
        ...
    def _isWebShopBundle(self, bundleID):
        ...
    def _getPrice(self, bundleID, priceKey):
        ...
    def _getBundles(self):
        ...
    def _getBonuses(self, bundleID):
        ...
    def _getConfig(self):
        ...
    def __updateSettings(self):
        ...
    def __handleTokensUpdate(self, diff):
        ...
