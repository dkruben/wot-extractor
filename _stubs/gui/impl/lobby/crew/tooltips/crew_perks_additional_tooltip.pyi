# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/tooltips/crew_perks_additional_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.tooltips.crew_perks_additional_tooltip_model import CrewPerksAdditionalTooltipModel as CrewPerksAdditionalTooltipModel
from gui.impl.gen.view_models.views.lobby.crew.tooltips.crew_perks_tooltip_model import BoosterType as BoosterType
from gui.impl.lobby.crew.crew_helpers import getTankmanCrewAssistOrderSets as getTankmanCrewAssistOrderSets
from gui.impl.lobby.crew.crew_helpers.model_setters import setSkillProgressionModel as setSkillProgressionModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.gui_items.Tankman import isSkillLearnt as isSkillLearnt, SKILL_EFFICIENCY_UNTRAINED as SKILL_EFFICIENCY_UNTRAINED, getBattleBooster as getBattleBooster
from gui.shared.gui_items.tankman_skill import getTankmanSkill as getTankmanSkill
from gui.shared.tooltips.advanced import SKILL_MOVIES as SKILL_MOVIES
from helpers import dependency as dependency
from items.components import perks_constants as perks_constants
from items.components.skills_constants import SKILLS_BY_ROLES_ORDERED as SKILLS_BY_ROLES_ORDERED
from skeletons.gui.game_control import IWotPlusController as IWotPlusController
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.gui_items.Tankman import Tankman as Tankman
from gui.shared.gui_items.tankman_skill import TankmanSkill as TankmanSkill
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle

class CrewPerksAdditionalTooltip(ViewImpl):
    _itemsCache: Any
    _wotPlusCtrl: Any
    __slots__: tuple
    _skillName: Any
    _tankman: Any
    _tankmanVehicle: Any
    _skill: Any
    _skillIdx: Any
    _skillBooster: Any
    _showCrewAssist: Any
    def __init__(self, skillName, skillRole, tankmanId=None, skillIdx=-1, showCrewAssist=False):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _fillModel(self):
        ...
    def _getVehicle(self):
        ...
    def _getBoosterType(self):
        ...
    def _isIrrelevant(self):
        ...
