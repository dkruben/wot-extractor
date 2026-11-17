# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/damage_log_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.Scaleform.daapi.view.battle.shared.damage_log_panel import DamageLogPanel as DamageLogPanel, _LogViewComponent as _LogViewComponent, _DamageActionImgVOBuilder as _DamageActionImgVOBuilder, _LogRecordVOBuilder as _LogRecordVOBuilder, _VehicleVOBuilder as _VehicleVOBuilder, _EMPTY_SHELL_VO_BUILDER as _EMPTY_SHELL_VO_BUILDER, _DAMAGE_VALUE_VO_BUILDER as _DAMAGE_VALUE_VO_BUILDER, _ReceivedHitVehicleVOBuilder as _ReceivedHitVehicleVOBuilder, _DamageShellVOBuilder as _DamageShellVOBuilder, _ShellVOBuilder as _ShellVOBuilder, _CritsShellVOBuilder as _CritsShellVOBuilder, _CriticalHitValueVOBuilder as _CriticalHitValueVOBuilder, _ActionImgVOBuilder as _ActionImgVOBuilder, _AssistActionImgVOBuilder as _AssistActionImgVOBuilder, _ShellModeImgVOBuilder as _ShellModeImgVOBuilder
from gui.battle_control.controllers.personal_efficiency_ctrl import _DamageEfficiencyInfo as _DamageEfficiencyInfo
from gui.battle_control.battle_constants import PERSONAL_EFFICIENCY_TYPE as _ETYPE
from gui.Scaleform.genConsts.BATTLEDAMAGELOG_IMAGES import BATTLEDAMAGELOG_IMAGES as _IMAGES
from gui.Scaleform.genConsts.BATTLE_EFFICIENCY_TYPES import BATTLE_EFFICIENCY_TYPES as BATTLE_EFFICIENCY_TYPES
from halloween.gui.scaleform.genConsts.HW_BATTLEDAMAGELOG_IMAGES import HW_BATTLEDAMAGELOG_IMAGES as _HW_IMAGES
from halloween.gui.scaleform.genConsts.HW_BATTLE_EFFICIENCY_TYPES import HW_BATTLE_EFFICIENCY_TYPES as HW_BATTLE_EFFICIENCY_TYPES
from halloween_common.halloween_constants import ATTACK_REASON as ATTACK_REASON
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from halloween.gui.hw_vehicle_role_helper import getVehicleRole as getVehicleRole
from halloween.gui.scaleform.daapi.view.battle.ribbons_panel import HWBattleRibbonsPanel as HWBattleRibbonsPanel
_HW_VEHICLE_CLASS_TAGS_ICONS: dict
_AGGREGATION_SETTINGS: dict
_HW_ETYPE_TO_RECORD_VO_BUILDER: dict

class HWReceivedHitVehicleVOBuilder(_ReceivedHitVehicleVOBuilder):
    def _populateVO(self, vehicleVO, info, arenaDP):
        ...

class HWExtendedDamageActionVOBuilder(_DamageActionImgVOBuilder):
    DEFAULT_DAMAGE_ICON = _IMAGES.DAMAGELOG_DAMAGE_16X16
    HW_ATTACK_REASON_TO_ICON: dict
    def _getImage(self, info):
        ...
    @classmethod
    def _getIcon(cls, reasonID, secondaryReasonID):
        ...

class HWExtendedReceivedDamageActionVOBuilder(HWExtendedDamageActionVOBuilder):
    DEFAULT_DAMAGE_ICON = _IMAGES.DAMAGELOG_DAMAGE_ENEMY_16X16
    HW_ATTACK_REASON_TO_ICON: dict

class HWVehicleVOBuilder(_VehicleVOBuilder):
    def _populateVO(self, vehicleVO, info, arenaDP):
        ...

class _HWDamageEfficiencyInfo(object):
    _damageEfficiencyInfo: Any
    _damage: Any
    def __init__(self, damageEfficiencyInfo):
        ...
    def __getattr__(self, name):
        ...
    def setDamage(self, damage):
        ...
    def getDamage(self):
        ...

class _HWLogViewComponent(_LogViewComponent):
    sessionProvider: Any
    _aggregatedEvents: Any
    _logViewMode: Any
    def __init__(self):
        ...
    def initialize(self, *args, **kwargs):
        ...
    def dispose(self):
        ...
    def updateViewMode(self, viewMode):
        ...
    def _buildLogMessageVO(self, info):
        ...
    def addToLog(self, events):
        ...
    def _onRibbonHidden(self, ribbon):
        ...

class HWDamageLogPanel(DamageLogPanel):
    _topLog: Any
    _bottomLog: Any
    __vehStateCtrl: Any
    def __init__(self):
        ...
    def _onVehicleControlling(self, vehicle):
        ...
