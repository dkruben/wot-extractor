# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/dialogs/sub_views/icon/item_icon.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from gui.impl.gen import R as R
from gui.impl.dialogs.sub_views.common import IconSetData as IconSetData
from gui.impl.dialogs.sub_views.icon.multiple_icons_set import MultipleIconsSet as MultipleIconsSet
from gui.impl.dialogs.sub_views.common.simple_text import ImageSubstitution as ImageSubstitution
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.Vehicle import getNationLessName as getNationLessName, getIconResourceName as getIconResourceName
from gui.shared.utils.functions import replaceHyphenToUnderscore as replaceHyphenToUnderscore
from helpers import dependency as dependency, int2roman as int2roman
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import TYPE_CHECKING as TYPE_CHECKING
from typing import List as List, Optional as Optional
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.shared.gui_items.artefacts import OptionalDevice as OptionalDevice
_logger: Any
ITEM_FORMATTERS: dict

class ItemIcons(MultipleIconsSet):
    __slots__: tuple
    _itemsCache: Any
    def __init__(self, items, isItemExchange=False):
        ...

def vehicleToIconSetDataFormatter(vehicle, backgrounds, overlays):
    ...
def optionalDeviceToIconSetDataFormatter(optDevice, backgrounds, overlays):
    ...
