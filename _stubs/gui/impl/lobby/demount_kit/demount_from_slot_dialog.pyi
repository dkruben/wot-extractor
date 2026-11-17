# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/demount_kit/demount_from_slot_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.dialogs.dialog_template import DialogTemplateView as DialogTemplateView
from gui.impl.dialogs.dialog_template_button import CancelButton as CancelButton, ConfirmButton as ConfirmButton
from gui.impl.dialogs.sub_views.content.simple_text_content import SimpleTextContent as SimpleTextContent
from gui.impl.dialogs.sub_views.title.simple_text_title import SimpleTextTitle as SimpleTextTitle
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.dialogs.template_settings.default_dialog_template_settings import DisplayFlags as DisplayFlags
from gui.impl.lobby.demount_kit.demount_kit_utils import getDemountDialogTitle as getDemountDialogTitle
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.impl.gen.view_models.views.dialogs.default_dialog_place_holders import DefaultDialogPlaceHolders as Placeholder

class DemountOptionalDeviceFromSlotDialog(DialogTemplateView):
    __slots__: tuple
    __itemsCache: Any
    __item: Any
    __forFitting: Any
    __vehicle: Any
    def __init__(self, itemCD, forFitting=False, vehicle=None, layoutID=None, uniqueID=None):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getAdditionalData(self):
        ...
    def _inventorySyncHandler(self, *_):
        ...
