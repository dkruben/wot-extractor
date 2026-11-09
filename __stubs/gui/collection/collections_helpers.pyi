# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/collection/collections_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
import SoundGroups as SoundGroups
import nations as nations
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from collections_common import UNUSABLE_COLLECTION_ENTITIES as UNUSABLE_COLLECTION_ENTITIES, USABLE_COLLECTION_ENTITIES as USABLE_COLLECTION_ENTITIES
from gui.collection.collections_constants import COLLECTION_ITEM_RES_KEY_TEMPLATE as COLLECTION_ITEM_RES_KEY_TEMPLATE, COLLECTION_RES_PREFIX as COLLECTION_RES_PREFIX
from gui.collection.sounds import Sounds as Sounds
from gui.customization.shared import getSingleVehicleForCustomization as getSingleVehicleForCustomization
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.collection.collection_item_preview_model import ItemType as ItemType
from gui.server_events.bonuses import getNonQuestBonuses as getNonQuestBonuses, mergeBonuses as mergeBonuses, splitBonuses as splitBonuses
from gui.shared.event_dispatcher import showBattlePass as showBattlePass, showHangar as showHangar, showStylePreview as showStylePreview, showStyleProgressionPreview as showStyleProgressionPreview, showCollectionWindow as showCollectionWindow
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from gui.sounds.filters import switchHangarFilteredFilter as switchHangarFilteredFilter
from helpers import dependency as dependency
from helpers.dependency import replace_none_kwargs as replace_none_kwargs
from items.tankmen import getNationConfig as getNationConfig, getNationGroups as getNationGroups
from shared_utils import findFirst as findFirst, first as first
from skeletons.gui.game_control import ICollectionsSystemController as ICollectionsSystemController, IBattlePassController as IBattlePassController
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import List as List, Dict as Dict, Optional as Optional, Tuple as Tuple, Union as Union
from collections_common import CollectionItem as CollectionItem
from frameworks.wulf import PyResAccessor as PyResAccessor
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle

# decorador original: @replace_none_kwargs(...)
def showCollectionStylePreview(styleCD, itemsCache=None):
    ...
# decorador original: @replace_none_kwargs(...)
def getVehicleForCollectionStyle(style, itemsCache=None):
    ...
def setHangarState():
    ...
def loadHangarFromCollections():
    ...
def loadBattlePassFromCollections(presenterID=None, chapterID=0):
    ...
# decorador original: @replace_none_kwargs(...)
def loadCollectionsFromBattlePass(battlePass=None):
    ...
# decorador original: @replace_none_kwargs(...)
def getItemInfo(itemId, collectionId, collections=None):
    ...
def getImagePath(imageResource):
    ...
def getItemResKey(collectionId, item):
    ...
# decorador original: @replace_none_kwargs(...)
def getCollectionRes(collectionId, collectionsSystem=None):
    ...
# decorador original: @replace_none_kwargs(...)
def getItemName(collectionId, item, collectionsSystem=None):
    ...
def getUsableItemName(item):
    ...
# decorador original: @replace_none_kwargs(...)
def getUnusableItemName(collectionId, item, collectionsSystem=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getCustomizationName(itemCD, itemsCache=None):
    ...
def getDossierName(itemName):
    ...
def getTankmanFullName(groupName):
    ...
def getItemPreviewType(item):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getCustomizationPreviewType(itemCD, itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getVehicleForStyleItem(item, itemsCache=None, collectionsSystem=None):
    ...
def composeBonuses(bonuses):
    ...
