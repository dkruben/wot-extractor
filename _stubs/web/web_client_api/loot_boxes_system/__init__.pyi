# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/loot_boxes_system/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from past.builtins import basestring as basestring
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.lootbox_system.base.bonuses_packers import mergeNeededBonuses as mergeNeededBonuses, processCompensationsWithLootbox as processCompensationsWithLootbox
from gui.lootbox_system.base.common import ViewID as ViewID, Views as Views
from gui.server_events.awards_formatters import AWARDS_SIZES as AWARDS_SIZES
from helpers import dependency as dependency
from skeletons.gui.game_control import ILootBoxSystemController as ILootBoxSystemController
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.gui.shared import IItemsCache as IItemsCache
from web.web_client_api import Field as Field, W2CSchema as W2CSchema, WebCommandException as WebCommandException, w2c as w2c, w2capi as w2capi
from web.web_client_api.common import ItemPackType as ItemPackType, ItemPackTypeGroup as ItemPackTypeGroup, sanitizeResPath as sanitizeResPath

class ViewsIDs(object):
    OVERLAY = 'overlay'
    SHOP = 'shop'
    ALL: tuple

class _LootBoxInfo(W2CSchema):
    id: Any
    full_info: Any

class _ShowViewSchema(W2CSchema):
    id: Any
    view_id: Any

class _ShowInfoSchema(W2CSchema):
    view_id: Any
    box_id: Any

# decorador original: @w2capi(...)
class LootBoxSystemWebApi(object):
    __lootBoxes: Any
    __itemsCache: Any
    __guiLoader: Any
    # decorador original: @w2c(...)
    def getLootBoxInfo(self, cmd):
        ...
    # decorador original: @w2c(...)
    def showBox(self, cmd):
        ...
    # decorador original: @w2c(...)
    def showInfoPage(self, cmd):
        ...
    def __addBonusesInfo(self, slotsInfo, eventName, fullInfo):
        ...
    @staticmethod
    def __isExistingBonus(bonusEntry, bonuses, fullInfo):
        ...

def _isValidViewID(_, data):
    ...
