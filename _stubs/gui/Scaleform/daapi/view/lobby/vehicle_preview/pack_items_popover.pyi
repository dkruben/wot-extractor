# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/pack_items_popover.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.lobby.vehicle_preview.items_kit_helper import lookupItem as lookupItem, showItemTooltip as showItemTooltip
from gui.Scaleform.daapi.view.meta.PackItemsPopoverMeta import PackItemsPopoverMeta as PackItemsPopoverMeta
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.utils import flashObject2Dict as flashObject2Dict
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from web.web_client_api.common import ItemPackEntry as ItemPackEntry, ItemPackType as ItemPackType
_R_SHOP_PACK = R.strings.tooltips.vehiclePreview.shopPack

class PackItemsPopover(PackItemsPopoverMeta):
    appLoader: Any
    itemsCache: Any
    goodiesCache: Any
    __data: Any
    __rawItems: Any
    __rawData: Any
    def __init__(self, ctx=None):
        ...
    def showTooltip(self, intCD, itemType):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
