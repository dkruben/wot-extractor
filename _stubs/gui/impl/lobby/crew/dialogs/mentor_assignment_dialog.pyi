# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/dialogs/mentor_assignment_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import typing as typing
import SoundGroups as SoundGroups
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.auxiliary.tankman_operations import packBaseTankman as packBaseTankman
from gui.impl.dialogs.dialog_template_button import CancelButton as CancelButton, ConfirmButton as ConfirmButton
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.dialogs.template_settings.default_dialog_template_settings import DisplayFlags as DisplayFlags
from gui.impl.gen.view_models.views.lobby.crew.common.tooltip_constants import TooltipConstants as TooltipConstants
from gui.impl.gen.view_models.views.lobby.crew.dialogs.mentor_assignment_dialog_model import MentorAssignmentDialogModel as MentorAssignmentDialogModel
from gui.impl.lobby.crew.crew_helpers.model_setters import setTmanMajorSkillsModel as setTmanMajorSkillsModel
from gui.impl.lobby.crew.crew_sounds import SOUNDS as SOUNDS
from gui.impl.lobby.crew.dialogs.base_crew_dialog_template_view import BaseCrewDialogTemplateView as BaseCrewDialogTemplateView
from gui.impl.lobby.crew.tooltips.empty_skill_tooltip import EmptySkillTooltip as EmptySkillTooltip
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from gui.shared.gui_items.Tankman import crewMemberRealSkillLevel as crewMemberRealSkillLevel
from gui.shared.gui_items.Vehicle import getTankmanIndex as getTankmanIndex
from helpers import dependency as dependency
from nations import NAMES as NAMES
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.gui_items import IGuiItemsFactory as IGuiItemsFactory
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from frameworks.wulf import ViewEvent as ViewEvent
from typing import Any as Any
from gui.shared.gui_items.Tankman import Tankman as Tankman
from gui.impl.gen.view_models.views.lobby.crew.dialogs.mentor_assignment_tankman_model import MentorAssignmentTankmanModel as MentorAssignmentTankmanModel

class MentorAssignmentDialog(BaseCrewDialogTemplateView):
    __slots__: tuple
    LAYOUT_ID: _Any
    VIEW_MODEL = MentorAssignmentDialogModel
    _itemsCache: _Any
    _itemsFactory: _Any
    _appLoader: _Any
    _toolTipMgr: _Any
    __sourceTankman: _Any
    __targetVehicle: _Any
    __targetTankman: _Any
    __totalXp: _Any
    __loseXp: _Any
    def __init__(self, sourceTmanId, targetTmanId):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _updateData(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __onInputChange(self, event):
        ...
    def __updateSubmitButton(self, isDisabled=True):
        ...
    def __getSkillLevel(self, isDonor, skillName, event):
        ...

def _packTankman(vmTankman, guiTankman):
    ...
