# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/container_vews/personal_file/components/skill_matrix_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import BigWorld as BigWorld
import typing as typing
from itertools import chain as chain
from constants import NEW_PERK_SYSTEM as NPS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.backport.backport_tooltip import createAndLoadBackportTooltipWindow as createAndLoadBackportTooltipWindow
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.common.skill.skill_model import BattleBooster as BattleBooster
from gui.impl.gen.view_models.views.lobby.crew.common.tooltip_constants import TooltipConstants as TooltipConstants
from gui.impl.gen.view_models.views.lobby.crew.personal_case.tankman_skill_model import TankmanSkillModel as TankmanSkillModel, AnimationType as AnimationType
from gui.impl.gen.view_models.views.lobby.crew.personal_case.tankman_skills_group_model import TankmanSkillsGroupModel as TankmanSkillsGroupModel
from gui.impl.lobby.container_views.base.components import ComponentBase as ComponentBase
from gui.impl.lobby.crew.crew_helpers.skill_model_setup import skillModelSetup as skillModelSetup
from gui.impl.lobby.crew.crew_helpers.tankman_helpers import getPerksResetGracePeriod as getPerksResetGracePeriod
from gui.impl.lobby.crew.tooltips.bonus_perks_tooltip import BonusPerksTooltip as BonusPerksTooltip
from gui.impl.lobby.crew.tooltips.empty_skill_tooltip import EmptySkillTooltip as EmptySkillTooltip
from gui.impl.lobby.crew.tooltips.qualification_tooltip import QualificationTooltip as QualificationTooltip
from gui.shared.gui_items.artefacts import TAG_CREW_BATTLE_BOOSTER as TAG_CREW_BATTLE_BOOSTER
from helpers import dependency as dependency
from items.tankmen import SKILLS_BY_ROLES as SKILLS_BY_ROLES, COMMON_SKILLS as COMMON_SKILLS
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.gui_items.tankman_skill import TankmanSkill as TankmanSkill
from frameworks.wulf import ViewEvent as ViewEvent
from gui.impl.gen.view_models.views.lobby.crew.personal_case.personal_file_view_model import PersonalFileViewModel as PersonalFileViewModel
from gui.impl.gen.view_models.views.lobby.crew.personal_case.skills_matrix_model import SkillsMatrixModel as SkillsMatrixModel
from typing import Any as Any, Callable as Callable, Iterable as Iterable, Optional as Optional, Tuple as Tuple

class SkillMatrixComponent(ComponentBase):
    itemsCache: _Any
    appLoader: _Any
    _toolTipMgr: _Any
    __isOnFocus: _Any
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
    def _getSkillAnimationType(self, tankmanSkillModel, index, isBonus=False):
        ...
    def _fillViewModel(self, vm):
        ...
    def _fillMajorSkills(self, vm):
        ...
    def _fillBonusSkills(self, vm):
        ...
    def _fillSkillsGroupModel(self, role, skills, gm, skillsLevels):
        ...
    def _getSkillModel(self, skill, level, role, index):
        ...
    def _fillGroupDirective(self, vm, role, isMajorRole):
        ...
    def _onIncrease(self):
        ...
    def _onReset(self):
        ...
    def _onSkillClick(self, kwargs):
        ...
    def _onSetAnimationInProgress(self, kwargs):
        ...
    def _onFocus(self, focused):
        ...
