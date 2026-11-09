# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/showcase_style_buying_preview.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.Scaleform.daapi.view.lobby.vehicle_preview.style_preview import VehicleStylePreview as VehicleStylePreview
from gui.Scaleform.genConsts.VEHPREVIEW_CONSTANTS import VEHPREVIEW_CONSTANTS as VEHPREVIEW_CONSTANTS
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Dict as Dict, Optional as Optional
from gui.shared.gui_items.customization.c11n_items import Style as Style

class VehicleShowcaseStyleBuyingPreview(VehicleStylePreview):
    __itemsCache: Any
    __style: Any
    __price: Any
    __originalPrice: Any
    __discountPercent: Any
    __endTime: Any
    __buyParams: Any
    __obtainingMethod: Any
    def __init__(self, ctx=None):
        ...
    def setBottomPanel(self, linkage=None):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def _populate(self):
        ...
    def _getAdditionalInfoVO(self):
        ...
    def _styleIsUnique(self):
        ...
    @staticmethod
    def __getVehicleInfoDescVO():
        ...
