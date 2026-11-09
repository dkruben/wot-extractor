# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/gui/Scaleform/daapi/view/battle/consumables_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from functools import partial as partial
import typing as typing
from Event import EventsSubscriber as EventsSubscriber
from comp7_core.gui.shared.tooltips.comp7_core_tooltips import getRoleEquipmentTooltipParts as getRoleEquipmentTooltipParts, getPoIEquipmentDescription as getPoIEquipmentDescription
from comp7_core_constants import ROLE_EQUIPMENT_TAG as ROLE_EQUIPMENT_TAG
from constants import ARENA_PERIOD as ARENA_PERIOD
from gui.Scaleform.daapi.view.battle.shared.consumables_panel import ConsumablesPanel as ConsumablesPanel
from gui.Scaleform.daapi.view.battle.shared.points_of_interest.poi_helpers import getPoiTypeByEquipment as getPoiTypeByEquipment
from gui.Scaleform.genConsts.ANIMATION_TYPES import ANIMATION_TYPES as ANIMATION_TYPES
from gui.Scaleform.genConsts.CONSUMABLES_PANEL_SETTINGS import CONSUMABLES_PANEL_SETTINGS as CONSUMABLES_PANEL_SETTINGS
from gui.battle_control import avatar_getter as avatar_getter
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.tooltips.consumables_panel import TOOLTIP_FORMAT as TOOLTIP_FORMAT
from gui.shared.utils.functions import stripColorTagDescrTags as stripColorTagDescrTags
from helpers import dependency as dependency
from points_of_interest_shared import PoiType as PoiType, POI_EQUIPMENT_TAG as POI_EQUIPMENT_TAG
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from typing import Optional as Optional
from comp7_core.gui.battle_control.controllers.consumables.comp7_equipment_ctrl import Comp7EquipmentController as Comp7EquipmentController
from gui.battle_control.arena_info.interfaces import IPrebattleSetupController as IPrebattleSetupController
from gui.battle_control.controllers.consumables.equipment_ctrl import _OrderItem as _OrderItem
_logger: Any

class Comp7CoreConsumablesPanel(ConsumablesPanel):
    __sessionProvider: Any
    _ROLE_EQUIPMENT_IDX = 6
    _POI_EQUIPMENT_IDX: dict
    _R_COMP7_EQUIPMENT_ICON = R.images.gui.maps.icons.roleSkills.c_43x43
    _R_POI_EQUIPMENT_ICON = R.images.gui.maps.icons.pointsOfInterest.equipments.c_43x43
    __es: Any
    def __init__(self):
        ...
    @property
    def _modeController(self):
        ...
    @property
    def __equipmentsCtrl(self):
        ...
    @property
    def __prebattleCtrl(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _getEquipmentIconPath(self, item):
        ...
    def _setEquipmentKeyHandler(self, item, bwKey, idx):
        ...
    def _onEquipmentAdded(self, intCD, item):
        ...
    def _updateEquipmentGlow(self, idx, item):
        ...
    def _buildEquipmentSlotTooltipText(self, item):
        ...
    def __addRoleEquipmentSlot(self, intCD, item):
        ...
    def __addPoiEquipmentSlot(self, intCD, item):
        ...
    def __updateRoleEquipmentState(self, state, previousState=None):
        ...
    def __updateRoleEquipmentCounter(self, value):
        ...
    def __updateRoleSkillAvailability(self):
        ...
    def __updatePrebattleRoleSkill(self):
        ...
    @staticmethod
    def __isRoleEquipment(item):
        ...
    @staticmethod
    def __isPoiEquipment(item):
        ...
    def __buildRoleEquipmentTooltipText(self):
        ...
    @staticmethod
    def __buildPoIEquipmentTooltipText(item, modeController):
        ...
