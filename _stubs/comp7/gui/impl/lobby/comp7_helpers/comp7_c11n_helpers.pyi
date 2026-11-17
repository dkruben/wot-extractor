# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/comp7_helpers/comp7_c11n_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from random import shuffle as shuffle
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from comp7.gui.shared.gui_items.dossier.stats import getComp7DossierStats as getComp7DossierStats
from comp7.gui.impl.lobby.comp7_helpers.comp7_shared import getComp7Criteria as getComp7Criteria
from comp7_common_const import qualificationQuestIDBySeasonNumber as qualificationQuestIDBySeasonNumber
from customization_quests_common import serializeToken as serializeToken
from gui.Scaleform.daapi.view.lobby.customization.context.editable_style_mode import EditableStyleMode as EditableStyleMode
from gui.Scaleform.daapi.view.lobby.customization.shared import CustomizationTabs as CustomizationTabs
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from items.components.c11n_constants import CustomizationType as CustomizationType
from shared_utils import first as first
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.gui_items import IGuiItemsFactory as IGuiItemsFactory
from typing import Optional as Optional, Union as Union, Dict as Dict, Tuple as Tuple, Callable as Callable, List as List
from gui.shared.gui_items.customization.c11n_items import Style as Style, Customization as Customization
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.shared.utils.requesters import RequestCriteria as RequestCriteria
from skeletons.gui.shared import IItemsRequester as IItemsRequester
_logger: Any

# decorador original: @dependency.replace_none_kwargs(...)
def getComp7ProgressionStyleCamouflage(styleID, branch, level, c11nService=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getComp7ProgressionStyle(seasonNum=None, comp7Ctrl=None, eventsCache=None, c11n=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getStylePreviewVehicle(style, defaultVehicle=None, itemsCache=None, comp7Controller=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def hasVehicleForCustomization(customization, itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getPreviewOutfit(style, branchID, progressLevel, vehicleCD, itemsFactory=None):
    ...
def isC11nItemTokenAttainable(allTokens, item, supportedTypes=...):
    ...
def getVehicleForStyle(items, criteria, sortKey, style, preferredVeh=None):
    ...
def getMaxLevelAndBattlesVehicleSortKey(items):
    ...
def selectStyleAndDecalInC11nHangar(c11n, items, styleCD, decalCD):
    ...
