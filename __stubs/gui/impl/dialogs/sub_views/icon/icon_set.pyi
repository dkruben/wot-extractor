# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/dialogs/sub_views/icon/icon_set.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from gui.impl.dialogs.sub_views.common import IconSetData as IconSetData
from gui.impl.dialogs.sub_views.icon.multiple_icons_set import MultipleIconsSet as MultipleIconsSet
from gui.impl.gen.view_models.views.dialogs.sub_views.multiple_icons_set_view_model import IconPositionLogicEnum as IconPositionLogicEnum
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import List as List, Optional as Optional
_logger: Any

class IconSet(MultipleIconsSet):
    __slots__: tuple
    _itemsCache: Any
    def __init__(self, iconResID, backgroundResIDList=None, overlayResIDList=None, layoutID=None, iconPositionLogic=...):
        ...
