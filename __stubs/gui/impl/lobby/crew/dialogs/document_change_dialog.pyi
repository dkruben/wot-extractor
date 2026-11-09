# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/dialogs/document_change_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import operator as operator
from .base_crew_dialog_template_view import BaseCrewDialogTemplateView as BaseCrewDialogTemplateView
from gui.impl import backport as backport
from gui.impl.dialogs.dialog_template_button import CancelButton as CancelButton, ConfirmButton as ConfirmButton
from gui.impl.dialogs.sub_views.icon.icon_set import IconSet as IconSet
from gui.impl.dialogs.sub_views.title.simple_text_title import SimpleTextTitle as SimpleTextTitle
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.dialogs.default_dialog_place_holders import DefaultDialogPlaceHolders as Placeholder
from gui.impl.gen.view_models.views.lobby.crew.dialogs.document_change_dialog_model import DocumentChangeDialogModel as DocumentChangeDialogModel
from gui.impl.lobby.crew.utils import getDocGroupValues as getDocGroupValues
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from gui.shared.gui_items.Tankman import getExtensionLessIconName as getExtensionLessIconName, getDynIconName as getDynIconName
from gui.shared.gui_items.items_actions import factory as factory
from helpers import dependency as dependency
from items import tankmen as tankmen
from skeletons.gui.shared import IItemsCache as IItemsCache

class DocumentChangeDialog(BaseCrewDialogTemplateView):
    __slots__: tuple
    LAYOUT_ID: Any
    VIEW_MODEL = DocumentChangeDialogModel
    _INVALID_IDX = -1
    _itemsCache: Any
    __tankmanInvID: Any
    __initialData: Any
    __firstNamesList: Any
    __lastNamesList: Any
    __firstNameIdx: Any
    __lastNameIdx: Any
    def __init__(self, tankmanInvID, ctx=None):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _updateViewModel(self, tankman):
        ...
    def _onChangeFirstName(self, args):
        ...
    def _onChangeLastName(self, args):
        ...
    def _setResult(self, result):
        ...
    def __updateSelectionIdxs(self):
        ...
    def __updateSubmitBtnModel(self, isDisabled=True):
        ...
    @staticmethod
    def __fillItemsList(vm, itemList, selectedItemName, selectedIdx):
        ...
