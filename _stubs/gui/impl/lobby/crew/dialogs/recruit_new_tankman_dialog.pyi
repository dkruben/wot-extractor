# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/dialogs/recruit_new_tankman_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from .base_crew_dialog_template_view import BaseCrewDialogTemplateView as BaseCrewDialogTemplateView
from gui import SystemMessages as SystemMessages
from gui.impl.dialogs.dialog_template_button import CancelButton as CancelButton, ConfirmButton as ConfirmButton
from gui.impl.gen.resources import R as R
from gui.impl.gen.view_models.views.lobby.crew.dialogs.recruit_new_tankman_dialog_model import RecruitNewTankmanDialogModel as RecruitNewTankmanDialogModel
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from gui.shared.gui_items.Tankman import NO_TANKMAN as NO_TANKMAN
from gui.shared.gui_items.processors.tankman import TankmanRecruitAndEquip as TankmanRecruitAndEquip, TankmanRecruit as TankmanRecruit
from gui.shared.utils import decorators as decorators
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES as SYSTEM_MESSAGES
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
_LOC = R.strings.dialogs.recruit
_FREE_INDEX = 0

class RecruitNewTankmanDialog(BaseCrewDialogTemplateView):
    __slots__: tuple
    LAYOUT_ID: Any
    VIEW_MODEL = RecruitNewTankmanDialogModel
    _itemsCache: Any
    _vehicle: Any
    _slotIdx: Any
    _putInTank: Any
    def __init__(self, vehicleCD, slotIdx, putInTank):
        ...
    @property
    def viewModel(self):
        ...
    def _getCallbacks(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onVehiclesInventoryUpdate(self, diff):
        ...
    def _updateViewModel(self):
        ...
    def _fillViewModel(self, vm):
        ...
    def _setResult(self, result):
        ...
    def _recruitTankman(self):
        ...
    def _processRecruit(self, operationKey):
        ...
    # decorador original: @decorators.adisp_process(...)
    def _processBuy(self, operationKey):
        ...
    # decorador original: @decorators.adisp_process(...)
    def _processBuyAndEquip(self, operationKey):
        ...
