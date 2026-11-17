# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/veh_skill_tree/rewards/prestige_milestone_achived_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import SoundGroups as SoundGroups
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer
from typing import Optional as Optional
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.impl.lobby.common.view_helpers import packBonusModelAndTooltipData as packBonusModelAndTooltipData
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.lobby.vehicle_hub.sub_presenters.veh_skill_tree.utils import getPrestigeBonus as getPrestigeBonus, getVehSkillTreeRewardViewBonusPacker as getVehSkillTreeRewardViewBonusPacker, PrestigeBonusContext as PrestigeBonusContext
from gui.prestige.prestige_helpers import getMilestones as getMilestones
from gui.Scaleform.daapi.view.lobby.customization.shared import CustomizationTabs as CustomizationTabs
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE, getItemTypeID as getItemTypeID
from helpers import dependency as dependency
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.veh_skill_tree.reward_screen_view_model import RewardScreenViewModel as RewardScreenViewModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.veh_skill_tree.vehicle_info_model import VehicleInfoModel as VehicleInfoModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.veh_skill_tree.rewards_slot_model import RewardStatus as RewardStatus

class PrestigeMilestoneAchivedView(ViewImpl):
    __itemsCache: Any
    __customizationService: Any
    __tooltipItems: Any
    __vehicle: Any
    __level: Any
    __bonus: Any
    def __init__(self, layoutID, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    def getTooltipData(self, event):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, vehCD, level):
        ...
    def _finalize(self):
        ...
    def __getBonus(self):
        ...
    def __fillReward(self, viewModel):
        ...
    def __fillVehicleInfo(self, viewModel):
        ...
    def __onRewardPreview(self):
        ...

class PrestigeMilestoneAchivedWindow(LobbyNotificationWindow):
    def __init__(self, vehCD, level, parent=None):
        ...
