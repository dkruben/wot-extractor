# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/tooltips/crew_perks_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import copy as copy
import typing as typing
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.tooltips.crew_perks_tooltip_booster_model import CrewPerksTooltipBoosterModel as CrewPerksTooltipBoosterModel
from gui.impl.gen.view_models.views.lobby.crew.tooltips.crew_perks_tooltip_model import BoosterType as BoosterType, CrewPerksTooltipModel as CrewPerksTooltipModel, PerkType as PerkType
from gui.impl.lobby.crew.crew_helpers.skill_helpers import formatDescription as formatDescription, getMaxSkillsEffAndLikeOwnVehTman as getMaxSkillsEffAndLikeOwnVehTman, getSkillDescription as getSkillDescription, getSkillParams as getSkillParams, getTmanWithSkill as getTmanWithSkill, getVehicleWithSkilledTman as getVehicleWithSkilledTman
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.gui_items.Tankman import crewMemberRealSkillLevel as crewMemberRealSkillLevel, getBattleBooster as getBattleBooster, getTankmanSkill as getTankmanSkill, isSkillLearnt as isSkillLearnt, tankmanPersonalSkillLevel as tankmanPersonalSkillLevel, SKILL_EFFICIENCY_UNTRAINED as SKILL_EFFICIENCY_UNTRAINED
from gui.shared.tooltips.advanced import SKILL_MOVIES as SKILL_MOVIES
from helpers import dependency as dependency
from items import tankmen as tankmen
from items.components import perks_constants as perks_constants
from items.components.skills_constants import UNLEARNABLE_SKILLS as UNLEARNABLE_SKILLS
from items.tankmen import MAX_SKILLS_EFFICIENCY as MAX_SKILLS_EFFICIENCY, MAX_SKILL_LEVEL as MAX_SKILL_LEVEL
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.gui_items import IGuiItemsFactory as IGuiItemsFactory
from gui.shared.gui_items.Tankman import Tankman as Tankman
from gui.shared.gui_items.tankman_skill import TankmanSkill as TankmanSkill
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle

class CrewPerksTooltip(ViewImpl):
    _itemsCache: Any
    _itemsFactory: Any
    __slots__: tuple
    _skillName: Any
    _showAdditionalInfo: Any
    _isAdvancedTooltipEnable: Any
    _customSkillType: Any
    _isBonus: Any
    _tankman: Any
    _tankmanVehicle: Any
    _isTmanTrainedVeh: Any
    _skillBooster: Any
    _skill: Any
    _isUntrained: Any
    _isIrrelevant: Any
    _skillLevelWithoutEff: Any
    _isFakeSkill: Any
    _isFakeSkillLvl: Any
    _isCmpSkill: Any
    _skillLevel: Any
    def __init__(self, skillName, skillRole, tankmanId, skillLevel=None, showAdditionalInfo=True, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getTankman(self, tankmanId, **kwargs):
        ...
    def _getVehicle(self, **kwargs):
        ...
    def _getIsIrrelevant(self):
        ...
    def _getBonusRole(self):
        ...
    def _isGroupSkill(self):
        ...
    def _isGroupSkillHasLowEff(self):
        ...
    def _isGroupSkillHasUntrained(self):
        ...
    def _fillModel(self):
        ...
    def fillCurrentLvlInfo(self, vm):
        ...
    def _getBoosterType(self):
        ...
    def __initSkillData(self, skillLevel):
        ...
    def __handleHoverNewSkill(self, skillBooster):
        ...
    def __handleHoverDisabledSkill(self, skillBooster):
        ...
    def __handleHoverLearnedSkill(self, skillBooster):
        ...
