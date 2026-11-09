# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/dialogs/skin_apply_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from .base_crew_dialog_template_view import BaseCrewDialogTemplateView as BaseCrewDialogTemplateView
from gui.impl.dialogs.dialog_template_button import CancelButton as CancelButton, ConfirmButton as ConfirmButton
from gui.impl.dialogs.sub_views.icon.icon_set import IconSet as IconSet
from gui.impl.dialogs.sub_views.title.simple_text_title import SimpleTextTitle as SimpleTextTitle
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.dialogs.default_dialog_place_holders import DefaultDialogPlaceHolders as Placeholder
from gui.impl.gen.view_models.views.lobby.crew.dialogs.skin_apply_dialog_model import SkinApplyDialogModel as SkinApplyDialogModel
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from gui.shared.gui_items.crew_skin import localizedFullName as localizedFullName
from gui.shared.gui_items.processors.tankman import CrewSkinEquip as CrewSkinEquip
from gui.shared.utils import decorators as decorators
from helpers import dependency as dependency, i18n as i18n
from skeletons.gui.shared import IItemsCache as IItemsCache

class SkinApplyDialog(BaseCrewDialogTemplateView):
    __slots__: tuple
    LAYOUT_ID: Any
    VIEW_MODEL = SkinApplyDialogModel
    _itemsCache: Any
    _crewSkinID: Any
    _tankManInvID: Any
    def __init__(self, crewSkinID, tankManInvID):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _setResult(self, result):
        ...
    # decorador original: @decorators.adisp_process(...)
    def _equipCrewSkin(self):
        ...
    def _updateViewModel(self):
        ...
    def _fillViewModel(self, vm):
        ...
