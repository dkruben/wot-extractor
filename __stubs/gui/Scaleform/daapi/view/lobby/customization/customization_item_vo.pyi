# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/customization/customization_item_vo.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers.AccountSettings import AccountSettings as AccountSettings, CUSTOMIZATION_STYLE_ITEMS_VISITED as CUSTOMIZATION_STYLE_ITEMS_VISITED
from gui.Scaleform.locale.VEHICLE_CUSTOMIZATION import VEHICLE_CUSTOMIZATION as VEHICLE_CUSTOMIZATION
from gui.customization.shared import PROJECTION_DECAL_FORM_TO_UI_ID as PROJECTION_DECAL_FORM_TO_UI_ID, PROJECTION_DECAL_IMAGE_FORM_TAG as PROJECTION_DECAL_IMAGE_FORM_TAG
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import getItemPricesVO as getItemPricesVO, text_styles as text_styles
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.gui_item_economics import ITEM_PRICE_EMPTY as ITEM_PRICE_EMPTY
from gui.shared.utils.graphics import isRendererPipelineDeferred as isRendererPipelineDeferred
from items.components.c11n_components import EditingStyleReason as EditingStyleReason
from items.components.c11n_constants import ProjectionDecalFormTags as ProjectionDecalFormTags, EDITING_STYLE_REASONS as EDITING_STYLE_REASONS
_ICON_ALPHA_BY_GUI_ITEM_TYPE: dict
_PROJECTION_DECAL_FORM_TO_IMAGE_SCALE: dict
_DEFAULT_IMAGE_SCALE = 1

class CustomizationCarouselRendererVO(object):
    __slots__: tuple
    intCD: Any
    typeId: Any
    isWide: Any
    icon: Any
    hasBonus: Any
    locked: Any
    buyPrice: Any
    quantity: Any
    isRental: Any
    autoRentEnabled: Any
    showDetailItems: Any
    customizationDisplayType: Any
    isSpecial: Any
    isDarked: Any
    isAlreadyUsed: Any
    showAlert: Any
    buyOperationAllowed: Any
    extraNames: Any
    showRareIcon: Any
    isEquipped: Any
    rentalInfoText: Any
    imageCached: Any
    noveltyCounter: Any
    editNoveltyCounter: Any
    isAllSeasons: Any
    formIconSource: Any
    defaultIconAlpha: Any
    lockText: Any
    isDim: Any
    formFactor: Any
    progressionLevel: Any
    editableIcon: Any
    editBtnEnabled: Any
    showEditableHint: Any
    showEditBtnHint: Any
    imageScale: Any
    tooltip: Any
    isChained: Any
    isUnsuitable: Any
    isProgressionRewindEnabled: Any
    isWithSerialNumber: Any
    isInProgress: Any
    isLinked: Any
    isNew: Any
    isRare: Any
    rarityIconSource: Any
    rarityBackgroundIconSource: Any
    showDisabled: Any
    def __init__(self, item, icon, hasBonus, locked, buyPrice, quantity=None, showDetailItems=True, isSpecial=False, isDarked=False, isAlreadyUsed=False, showAlert=False, buyOperationAllowed=True, extraNames=None, isEquipped=False, rentalInfoText='', imageCached=True, noveltyCounter=0, editNoveltyCounter=0, autoRentEnabled=False, formIconSource='', defaultIconAlpha=1, lockText='', formFactor=-1, progressionLevel=-1, imageScale=1, editableIcon='', editBtnEnabled=False, showEditableHint=False, showEditBtnHint=False, tooltip='', isChained=False, isUnsuitable=False, isProgressionRewindEnabled=False, isWithSerialNumber=False, isInProgress=False, isLinked=False, isNew=False, isRare=False, rarityIconSource='', rarityBackgroundIconSource='', showDisabled=False):
        ...
    def asDict(self):
        ...

def buildCustomizationItemDataVO(item, count=None, isApplied=False, isDarked=False, isUsedUp=False, autoRentEnabled=False, vehicle=None, progressionLevel=None, icon=None, showDetailItems=True, plainView=False, showEditableHint=False, showEditBtnHint=False, isChained=False, isUnsuitable=False, isInProgress=False, rarity=''):
    ...
def __getIcon(item, progressionLevel):
    ...
def __isItemSpecial(item):
    ...
def __isNeedToShowAlert(item):
    ...
def __getEditableBlockData(item, vehicle=None):
    ...
