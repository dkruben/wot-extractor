# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/damage_log_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.Scaleform.daapi.view.battle.shared.damage_log_panel import DamageLogPanel as DamageLogPanel, _LogViewComponent as _LogViewComponent, _DamageActionImgVOBuilder as _DamageActionImgVOBuilder, _LogRecordVOBuilder as _LogRecordVOBuilder, _VehicleVOBuilder as _VehicleVOBuilder, _EMPTY_SHELL_VO_BUILDER as _EMPTY_SHELL_VO_BUILDER, _DAMAGE_VALUE_VO_BUILDER as _DAMAGE_VALUE_VO_BUILDER, _ReceivedHitVehicleVOBuilder as _ReceivedHitVehicleVOBuilder, _DamageShellVOBuilder as _DamageShellVOBuilder, _ShellVOBuilder as _ShellVOBuilder, _CritsShellVOBuilder as _CritsShellVOBuilder, _CriticalHitValueVOBuilder as _CriticalHitValueVOBuilder, _ActionImgVOBuilder as _ActionImgVOBuilder, _AssistActionImgVOBuilder as _AssistActionImgVOBuilder, _ShellModeImgVOBuilder as _ShellModeImgVOBuilder
from gui.battle_control.battle_constants import PERSONAL_EFFICIENCY_TYPE as _ETYPE
from gui.Scaleform.genConsts.BATTLEDAMAGELOG_IMAGES import BATTLEDAMAGELOG_IMAGES as _IMAGES
from last_stand.gui.scaleform.genConsts.LS_BATTLEDAMAGELOG_IMAGES import LS_BATTLEDAMAGELOG_IMAGES as _LS_IMAGES
from last_stand_common.last_stand_constants import ATTACK_REASON as ATTACK_REASON
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from last_stand.gui.ls_vehicle_role_helper import getVehicleRole as getVehicleRole
_LS_VEHICLE_CLASS_TAGS_ICONS: dict
_LS_ETYPE_TO_RECORD_VO_BUILDER: dict

class LSReceivedHitVehicleVOBuilder(_ReceivedHitVehicleVOBuilder):
    def _populateVO(self, vehicleVO, info, arenaDP):
        ...

class LSExtendedDamageActionVOBuilder(_DamageActionImgVOBuilder):
    DEFAULT_DAMAGE_ICON = _IMAGES.DAMAGELOG_DAMAGE_16X16
    LS_ATTACK_REASON_TO_ICON: dict
    def _getImage(self, info):
        ...
    @classmethod
    def _getIcon(cls, reasonID):
        ...

class LSExtendedReceivedDamageActionVOBuilder(LSExtendedDamageActionVOBuilder):
    DEFAULT_DAMAGE_ICON = _IMAGES.DAMAGELOG_DAMAGE_ENEMY_16X16
    LS_ATTACK_REASON_TO_ICON: dict

class LSVehicleVOBuilder(_VehicleVOBuilder):
    def _populateVO(self, vehicleVO, info, arenaDP):
        ...

class _LSLogViewComponent(_LogViewComponent):
    sessionProvider: Any
    _logViewMode: Any
    def updateViewMode(self, viewMode):
        ...
    def _buildLogMessageVO(self, info):
        ...

class LSDamageLogPanel(DamageLogPanel):
    _topLog: Any
    _bottomLog: Any
    __vehStateCtrl: Any
    def __init__(self):
        ...
    def _onVehicleControlling(self, vehicle):
        ...
