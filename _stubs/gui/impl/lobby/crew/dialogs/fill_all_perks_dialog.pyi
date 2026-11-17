# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/dialogs/fill_all_perks_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.dialogs.dialog_template_button import ConfirmButton as ConfirmButton, CancelButton as CancelButton
from gui.impl.gen.resources import R as R
from gui.impl.gen.view_models.views.lobby.crew.common.tooltip_constants import TooltipConstants as TooltipConstants
from gui.impl.gen.view_models.views.lobby.crew.dialogs.fill_all_perks_dialog_model import FillAllPerksDialogModel as FillAllPerksDialogModel
from gui.impl.gen.view_models.views.lobby.crew.dialogs.fill_all_perks_dialog_row import FillAllPerksDialogRow as FillAllPerksDialogRow
from gui.impl.lobby.crew.dialogs.recruit_window.base_crew_dialog_template_with_blur_view import BaseCrewDialogTemplateWithBlurView as BaseCrewDialogTemplateWithBlurView
from helpers import dependency as dependency
from items.components.skills_constants import ORDERED_ROLES as ORDERED_ROLES
from items.tankmen_cfg import getAutoFillConfig as getAutoFillConfig
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.shared import IItemsCache as IItemsCache

class FillAllPerksDialog(BaseCrewDialogTemplateWithBlurView):
    itemsCache: Any
    __slots__: tuple
    LAYOUT_ID: Any
    VIEW_MODEL = FillAllPerksDialogModel
    __appLoader: Any
    __appliedForBarracks: Any
    __toolTipMgr: Any
    def __init__(self, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTip(self, event):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _getAdditionalData(self):
        ...
    def _onChange(self):
        ...
