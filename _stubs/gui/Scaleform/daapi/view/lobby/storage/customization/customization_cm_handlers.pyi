# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/storage/customization/customization_cm_handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
from adisp import adisp_process as adisp_process
from gui import DialogsInterface as DialogsInterface
from gui.Scaleform.daapi.view.dialogs.confirm_customization_item_dialog_meta import ConfirmC11nSellMeta as ConfirmC11nSellMeta
from gui.Scaleform.daapi.view.lobby.shared.cm_handlers import option as option, CMLabel as CMLabel, ContextMenu as ContextMenu
from gui.Scaleform.daapi.view.lobby.storage.storage_helpers import isCustomizationAvailableForSell as isCustomizationAvailableForSell, getAvailableForSellCustomizationCount as getAvailableForSellCustomizationCount
from gui.Scaleform.daapi.view.lobby.storage.storage_helpers import customizationPreview as customizationPreview
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity as EventSystemEntity
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from helpers import dependency as dependency
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.shared import IItemsCache as IItemsCache

class CustomizationCMHandler(ContextMenu, EventSystemEntity):
    __service: Any
    __itemsCache: Any
    __sqGen: Any
    _id: Any
    _vehicleCD: Any
    # decorador original: @option(...)
    def preview(self):
        ...
    # decorador original: @option(...)
    # decorador original: @adisp_process
    def sell(self):
        ...
    def _initFlashValues(self, ctx):
        ...
    def _getOptionCustomData(self, label):
        ...
    def __sellItem(self, itemCD, count, vehicle):
        ...
