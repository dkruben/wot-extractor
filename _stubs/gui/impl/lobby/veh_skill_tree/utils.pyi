# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/veh_skill_tree/utils.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from typing import Dict as Dict, Optional as Optional
from helpers import dependency as dependency
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.veh_skill_tree.node_model import Type as Type, Status as Status, NodeModel as NodeModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.veh_skill_tree.rewards_slot_model import RewardsSlotModel as RewardsSlotModel
from frameworks.wulf.view.array import fillStringsArray as fillStringsArray
from gui.server_events.bonuses import getNonQuestBonuses as getNonQuestBonuses, CustomizationsBonus as CustomizationsBonus
from gui.shared.gui_items import Vehicle as Vehicle
from gui.shared.missions.packers.bonus import CustomizationBonusUIPacker as CustomizationBonusUIPacker, BonusUIPacker as BonusUIPacker
from gui.shared.missions.packers.bonus import getDefaultBonusPackersMap as getDefaultBonusPackersMap
from gui.veh_post_progression.models.progression_step import PostProgressionStepItem as PostProgressionStepItem
from post_progression_common import VehicleState as VehicleState
from prestige_system.prestige_milestones_common import PrestigeLevelType as PrestigeLevelType, MilestonesType as MilestonesType
from skeletons.gui.shared import IItemsCache as IItemsCache
PrestigeBonusContext: Any

class PrestigeCustomizationBonusUIPacker(CustomizationBonusUIPacker):
    __itemsCache: Any
    @classmethod
    def _getBonusModel(cls):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus, item, label):
        ...

def getVehSkillTreeBonusPackersMap():
    ...
def getVehSkillTreeRewardViewBonusPacker():
    ...
def getPrestigeBonus(milestones, ctx):
    ...
def fillNodeModel(nodeVM, step, nodeStatus):
    ...
def getCheapestAvailablePerk(vehicle):
    ...
def getFullProgressionState(vehicle):
    ...
