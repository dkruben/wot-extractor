# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/impl/lobby/presenters/frontline_ability_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import viewitems as viewitems
from frontline.gui.frontline_helpers import AbilitiesTemplates as AbilitiesTemplates, getFrontlineState as getFrontlineState
from frontline.gui.frontline_helpers import getSkillParams as getSkillParams
from frontline.gui.impl.gen.view_models.views.lobby.components.loadout.battle_abilities_setup_model import BattleAbilitiesSetupModel as BattleAbilitiesSetupModel
from frontline.gui.impl.gen.view_models.views.lobby.components.loadout.battle_ability_details import BattleAbilityDetails as BattleAbilityDetails
from frontline.gui.impl.gen.view_models.views.lobby.components.loadout.battle_ability_level_model import BattleAbilityLevelModel as BattleAbilityLevelModel
from frontline.gui.impl.gen.view_models.views.lobby.components.loadout.battle_ability_level_param_model import BattleAbilityLevelParamModel as BattleAbilityLevelParamModel
from frontline.gui.impl.gen.view_models.views.lobby.views.frontline_const import FrontlineConst as FrontlineConst
from frontline.gui.impl.lobby.tank_setup.array_provider import BattleAbilityProvider as BattleAbilityProvider
from frontline.gui.impl.lobby.tank_setup.configuration import EpicBattleTabs as EpicBattleTabs
from frontline.gui.impl.lobby.tank_setup.interactor import FrontlineInteractor as FrontlineInteractor
from frontline.gui.impl.lobby.tooltips.skill_order_tooltip import SkillOrderTooltip as SkillOrderTooltip
import SoundGroups as SoundGroups
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from account_helpers.settings_core.options import KeyboardSetting as KeyboardSetting
from epic_constants import CATEGORIES_ORDER as CATEGORIES_ORDER
from frameworks.wulf import Array as Array
from gui.game_control.epic_meta_game_ctrl import EpicMetaGameSkill as EpicMetaGameSkill
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_panel_constants import AmmunitionPanelConstants as AmmunitionPanelConstants
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel as BaseSetupModel
from gui.impl.lobby.hangar.presenters.loadout_presenter_base import LoadoutPresenterBase as LoadoutPresenterBase, LoadoutEntityProvider as LoadoutEntityProvider
from gui.impl.lobby.tank_setup.array_providers.base import BaseVehSectionContext as BaseVehSectionContext
from gui.impl.lobby.tank_setup.tank_setup_sounds import TankSetupSoundEvents as TankSetupSoundEvents
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from helpers import dependency as dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController
from skeletons.gui.shared import IItemsCache as IItemsCache
from wg_async import wg_async as wg_async, await_callback as await_callback
from gui.impl.lobby.tank_setup.interactors.base import InteractingItem as InteractingItem
TEMPLATES: Any

# base nao representavel no stub: LoadoutPresenterBase[...]
class FrontlineAbilityPresenter:
    __epicController: Any
    __itemsCache: Any
    _sectionName: Any
    _guiItemType: Any
    _currentSectionName: Any
    _pendingPurchaseSkillIds: Any
    _pendingPurchaseItemIntCDs: Any
    _itemDetailsLevelMap: Any
    _totalPurchasePrice: Any
    _selectedSlotId: Any
    __gameModeStatus: Any
    __epicSkills: Any
    __slotSelectionObserver: Any
    _provider: Any
    def __init__(self, interactingItem, slotSelectionObserver):
        ...
    def createSlotActions(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def updateBlock(self, viewModel):
        ...
    def _getKeySettings(self):
        ...
    def _getSlotIdxByCategory(self, category):
        ...
    @property
    def _vehicle(self):
        ...
    def _revertItem(self, slotID):
        ...
    def _selectItem(self, slotID, itemCD):
        ...
    def _getEvents(self):
        ...
    def _createProvider(self, vehInteractingItem):
        ...
    def _updateModel(self, *_):
        ...
    def _onRevertItem(self, args):
        ...
    def _onSlotSelected(self, slotIndex, sectionName, sectionSwitched):
        ...
    def _onAdd(self, args):
        ...
    def _update(self):
        ...
    def __applyAbilitiesToTypeSettings(self, state):
        ...
    def __updateProvider(self):
        ...
    def __updateDetails(self):
        ...
    def __fillDetailsSkillLevels(self, levels, skillData):
        ...
    # decorador original: @wg_async
    def __onDealCancelled(self, _=None):
        ...
    def __onApplyToTypeChanged(self, *_):
        ...
    def __onBattleAbilitiesUpdated(self):
        ...
    def __onEpicUpdated(self, diff):
        ...
    def __onChangedVehicle(self):
        ...
    def __onCurrentAbilityLevelChanged(self, params):
        ...
    def __getCurrentLayoutItem(self, slotId):
        ...
    def __onGameModeStatusChange(self):
        ...
