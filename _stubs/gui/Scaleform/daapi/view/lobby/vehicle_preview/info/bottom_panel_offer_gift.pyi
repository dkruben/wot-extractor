# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/info/bottom_panel_offer_gift.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.Scaleform.daapi.view.lobby.vehicle_preview.items_kit_helper import lookupItem as lookupItem, showItemTooltip as showItemTooltip
from gui.Scaleform.daapi.view.meta.VehiclePreviewBottomPanelOfferGiftMeta import VehiclePreviewBottomPanelOfferGiftMeta as VehiclePreviewBottomPanelOfferGiftMeta
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache
from skeletons.gui.shared import IItemsCache as IItemsCache

class VehiclePreviewBottomPanelOfferGift(VehiclePreviewBottomPanelOfferGiftMeta):
    __goodiesCache: Any
    __itemsCache: Any
    __appLoader: Any
    __items: Any
    __confirmCallback: Any
    def __init__(self, ctx=None):
        ...
    def setData(self, itemsPack, panelDataVO, packedItemsVO, confirmCallback):
        ...
    def onBuyClick(self):
        ...
    def showTooltip(self, intCD, itemType):
        ...
