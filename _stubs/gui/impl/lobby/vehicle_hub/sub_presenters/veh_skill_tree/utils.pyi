# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/vehicle_hub/sub_presenters/veh_skill_tree/utils.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import namedtuple as namedtuple
from helpers import dependency as dependency
from items import vehicles as vehicles
from gui.impl import backport as backport
from gui.impl.backport import TooltipData as TooltipData
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.veh_skill_tree.node_model import Type as Type, Status as Status
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.veh_skill_tree.rewards_slot_model import RewardsSlotModel as RewardsSlotModel
from gui.impl.gen.view_models.views.lobby.veh_skill_tree.tooltips.prestige_reward_tooltip_model import RewardsSlotTooltipModel as RewardsSlotTooltipModel
from frameworks.wulf.view.array import fillStringsArray as fillStringsArray
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE, getItemTypeID as getItemTypeID
from gui.shared.gui_items.customization import CustomizationTooltipContext as CustomizationTooltipContext
from gui.server_events.bonuses import getNonQuestBonuses as getNonQuestBonuses
from gui.shared.gui_items.Vehicle import getNationLessName as getNationLessName
from gui.shared.missions.packers.bonus import CustomizationBonusUIPacker as CustomizationBonusUIPacker, BonusUIPacker as BonusUIPacker
from gui.shared.missions.packers.bonus import getDefaultBonusPackersMap as getDefaultBonusPackersMap
from post_progression_common import VehicleState as VehicleState
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Dict as Dict, List as List, Optional as Optional, Tuple as Tuple
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.veh_skill_tree.node_model import NodeModel as NodeModel
from gui.server_events.bonuses import CustomizationsBonus as CustomizationsBonus
from gui.shared.gui_items import Vehicle as Vehicle
from gui.shared.gui_items.customization.c11n_items import Customization as Customization
from gui.veh_post_progression.models.progression_step import PostProgressionStepItem as PostProgressionStepItem
from prestige_system.prestige_milestones_common import PrestigeLevelType as PrestigeLevelType, MilestonesType as MilestonesType
PrestigeBonusContext: Any

class PrestigeCustomizationBonusUIPacker(CustomizationBonusUIPacker):
    __itemsCache: Any
    @classmethod
    def _getBonusModel(cls):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus, item, label):
        ...
    @classmethod
    def _getToolTip(cls, bonus):
        ...
    @classmethod
    def _getToolTipData(cls, itemCustomization, vehCD=-1):
        ...
    @staticmethod
    def getTextInfoByItemTypeID(itemTypeID):
        ...

class PrestigeCustomizationTooltipBonusUIPacker(CustomizationBonusUIPacker):
    @classmethod
    def _getBonusModel(cls):
        ...
    @classmethod
    def _packSingleBonus(cls, bonus, item, label):
        ...

def getVehSkillTreeRewardViewBonusPacker():
    ...
def getVehSkillTreeRewardTooltipViewBonusPacker():
    ...
def getPrestigeBonus(milestones, ctx):
    ...
def fillNodeModel(nodeVM, step, nodeStatus, vehicle):
    ...
def getFullProgressionState(vehicle):
    ...
def getCheapestAvailablePerk(vehicle):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getEliteExpirience(exclude=..., itemsCache=None):
    ...
def constructNodeUiId(uniqueId, nodeId):
    ...
def deconstructNodeUiId(uniqueId, nodeUiId):
    ...
