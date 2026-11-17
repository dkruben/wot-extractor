# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/veh_post_progression/dialogs/destroy_pair_modification.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import iteritems as iteritems
from gui.impl import backport as backport
from gui.impl.dialogs.dialog_template import DialogTemplateView as DialogTemplateView
from gui.impl.dialogs.dialog_template_button import ConfirmButton as ConfirmButton, CancelButton as CancelButton
from gui.impl.dialogs.sub_views.content.simple_text_content import SimpleTextContent as SimpleTextContent
from gui.impl.dialogs.sub_views.icon.icon_set import IconSet as IconSet
from gui.impl.dialogs.sub_views.title.simple_text_title import SimpleTextTitle as SimpleTextTitle
from gui.impl.dialogs.sub_views.top_right.money_balance import MoneyBalance as MoneyBalance
from gui.impl.gen.view_models.views.dialogs.default_dialog_place_holders import DefaultDialogPlaceHolders as DefaultDialogPlaceHolders
from gui.impl.gen import R as R
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from shared_utils import first as first
_R_PATH = R.strings.veh_post_progression.destroyPairModificationsDialog

class DestroyPairModificationsDialog(DialogTemplateView):
    __itemsCache: Any
    __slots__: tuple
    __vehicle: Any
    __stepIDs: Any
    def __init__(self, layoutID=None, uniqueID=None, **kwargs):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __getTitleText(self):
        ...
    def __getDescriptionText(self):
        ...
    def __onInventoryResync(self, _, diff):
        ...
    def __updatePrice(self, contentModel):
        ...
    def __checkDestroy(self):
        ...
