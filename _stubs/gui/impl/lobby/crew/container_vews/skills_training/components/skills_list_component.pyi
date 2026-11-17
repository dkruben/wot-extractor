# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/container_vews/skills_training/components/skills_list_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import logging as logging
from functools import partial as partial
import typing as typing
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.common.tooltip_constants import TooltipConstants as TooltipConstants
from gui.impl.gen.view_models.views.lobby.crew.skill_training_model import SkillTrainingModel as SkillTrainingModel
from gui.impl.gen.view_models.views.lobby.crew.sort_dropdown_item_model import SortingTypeEnum as SortingTypeEnum
from gui.impl.lobby.common.tooltips.extended_text_tooltip import ExtendedTextTooltip as ExtendedTextTooltip
from gui.impl.lobby.container_views.base.components import ComponentBase as ComponentBase
from gui.impl.lobby.crew.container_vews.skills_training import loadSortingOrderType as loadSortingOrderType
from gui.impl.lobby.crew.crew_helpers import getTankmanCrewAssistOrderSets as getTankmanCrewAssistOrderSets
from gui.impl.lobby.crew.crew_helpers.skill_helpers import formatDescription as formatDescription, getSkillParams as getSkillParams
from gui.impl.lobby.crew.crew_helpers.skill_model_setup import skillModelSetup as skillModelSetup
from gui.shared.gui_items.Tankman import Target as Target
from helpers import dependency as dependency
from items.components.skills_constants import COMMON_ROLE as COMMON_ROLE
from items.tankmen import MAX_SKILL_LEVEL as MAX_SKILL_LEVEL
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from typing import Any as Any, Callable as Callable, Tuple as Tuple
from gui.impl.gen.view_models.views.lobby.crew.skills_training_view_model import SkillsTrainingViewModel as SkillsTrainingViewModel
from gui.impl.gen.view_models.views.lobby.crew.skills_list_model import SkillsListModel as SkillsListModel
from gui.shared.gui_items.tankman_skill import TankmanSkill as TankmanSkill
from skeletons.gui.game_control import IWotPlusController as IWotPlusController
_logger: _Any

class SkillsListComponent(ComponentBase):
    __slots__: tuple
    __appLoader: _Any
    __toolTipMgr: _Any
    def __init__(self, key, parent):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _getViewModel(self, vm):
        ...
    def _getEvents(self):
        ...
    def _fillViewModel(self, vm):
        ...
    def __fillMajorSkillsList(self, skillsByRoles, commonSkillsList, regularSkillsList, irrelevantSkillsList, popularityData, popularitySortFunction):
        ...
    def __fillBonusSkillsList(self, skillsByRoles, regularSkillsList, popularityData, popularitySortFunction):
        ...
    def __fillSkillsList(self, skillsListVM, skills, checkIrrelevant=True, popularityData=None, sortFunction=None):
        ...
    def _onSkillHover(self, kwargs):
        ...
    def _onSkillOut(self, kwargs):
        ...
    def _onSkillClick(self, kwargs):
        ...
    def __onTrain(self):
        ...
    def __onCancel(self):
        ...
    def __getCrewAssistPopularityData(self):
        ...
