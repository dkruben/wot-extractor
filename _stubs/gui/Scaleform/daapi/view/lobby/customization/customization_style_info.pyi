# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/customization/customization_style_info.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui import makeHtmlString as makeHtmlString
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.daapi.view.lobby.customization.shared import getSuitableText as getSuitableText
from gui.Scaleform.daapi.view.meta.CustomizationStyleInfoMeta import CustomizationStyleInfoMeta as CustomizationStyleInfoMeta
from gui.shared.gui_items.gui_item_economics import ITEM_PRICE_EMPTY as ITEM_PRICE_EMPTY
from gui.shared.utils.graphics import isRendererPipelineDeferred as isRendererPipelineDeferred
from gui.shared.view_helpers.blur_manager import CachedBlur as CachedBlur
from gui.customization.shared import C11nId as C11nId, getTotalPurchaseInfo as getTotalPurchaseInfo
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from helpers import dependency as dependency
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from items.components.c11n_constants import SeasonType as SeasonType
from math_common import round_py2_style as round_py2_style
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.shared import IItemsCache as IItemsCache
from vehicle_outfit.outfit import Area as Area
StyleInfoVO: Any
ButtonVO: Any
ParamVO: Any
STYLE_INFO_BLUR_DELAY = 0.2
BACKGROUND_ALPHA_FORWARD = 1.0
BACKGROUND_ALPHA_DEFERRED = 0.5
_INSERTION_OPEN_TAG = "<font size='16' face='$FieldFont' color='#E9E2BF'>"
_INSERTION_OPEN_TAG_BIG = "<font size='18' face='$TitleFont' color='#E9E2BF'>"
_INSERTION_CLOSE_TAG = '</font>'

class CustomizationStyleInfo(CustomizationStyleInfoMeta, CallbackDelayer):
    service: Any
    itemsCache: Any
    __ctx: Any
    __blur: Any
    __blurRectId: Any
    __visible: Any
    __prevStyle: Any
    __selectedStyle: Any
    __paramsDOF: Any
    __blurParams: Any
    @property
    def visible(self):
        ...
    def __init__(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def show(self, style=None):
        ...
    def updateButton(self, *_):
        ...
    def onClose(self):
        ...
    def onApply(self):
        ...
    def hide(self):
        ...
    def disableBlur(self):
        ...
    def __makeVO(self, style):
        ...
    def __makeButtonVO(self):
        ...
    def __makeParamsVO(self, style):
        ...
    def __enableBlur(self):
        ...
    def __installStyle(self, style):
        ...
    def __onUpdateStyleInfoDOF(self, paramsDOF):
        ...
    def __onCustomizationHelperRecreated(self):
        ...
    def __onVehicleChangeStarted(self):
        ...
    def onWidthUpdated(self, x, width, height):
        ...
    def __setBackgroundAlpha(self):
        ...
