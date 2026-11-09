# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/base/account_styles.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import Event as Event
from gui.impl.lobby.hangar.base.hangar_interfaces import IAccountStyles as IAccountStyles
from gui.impl.lobby.hangar.presenters.utils import take3DStyles as take3DStyles
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA, RequestCriteria as RequestCriteria
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
UPDATES: tuple

class AccountStyles(IAccountStyles):
    _customizationService: Any
    _itemsCache: Any
    __styleCriteria: Any
    __vehiclesWith3Dstyles: Any
    onChanged: Any
    def __init__(self):
        ...
    @property
    def criteria(self):
        ...
    @property
    def vehiclesWith3DStyles(self):
        ...
    def initialize(self):
        ...
    def destroy(self):
        ...
    def recalculate(self):
        ...
    def __updateCriteria(self):
        ...
    def __onCacheResync(self, reason, diff):
        ...
