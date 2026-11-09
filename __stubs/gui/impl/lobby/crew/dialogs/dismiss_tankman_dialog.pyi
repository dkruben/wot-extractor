# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/dialogs/dismiss_tankman_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from .base_crew_dialog_template_view import BaseCrewDialogTemplateView as BaseCrewDialogTemplateView
from gui.impl.dialogs.dialog_template_button import CancelButton as CancelButton, ConfirmButton as ConfirmButton
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.dialogs.dismiss_tankman_dialog_model import DismissTankmanDialogModel as DismissTankmanDialogModel
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.crew.crew_helpers.model_setters import setTankmanModel as setTankmanModel, setReplacedTankmanModel as setReplacedTankmanModel, setTmanSkillsModel as setTmanSkillsModel
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from gui.shared.gui_items.Tankman import Tankman as Tankman, MAX_ROLE_LEVEL as MAX_ROLE_LEVEL
from gui.shared.gui_items.items_actions import factory as factory
from helpers import dependency as dependency, time_utils as time_utils
from skeletons.gui.game_control import IRestoreController as IRestoreController
from skeletons.gui.shared import IItemsCache as IItemsCache

class DismissTankmanDialog(BaseCrewDialogTemplateView):
    __slots__: tuple
    LAYOUT_ID: Any
    VIEW_MODEL = DismissTankmanDialogModel
    _itemsCache: Any
    _restoreCtrl: Any
    _tankman: Any
    def __init__(self, tankmanId, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    # decorador original: @args2params(...)
    def _onInputChanged(self, value):
        ...
    def _setResult(self, result):
        ...
    def _updateViewModel(self):
        ...
    def _fillViewModel(self, vm):
        ...
