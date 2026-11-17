# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/battle/damage_log_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl import backport as backport
from helpers import dependency as dependency
from gui.Scaleform.daapi.view.battle.shared.damage_log_panel import DamageLogPanel as DamageLogPanel, _LogViewComponent as _LogViewComponent, _DamageActionImgVOBuilder as _DamageActionImgVOBuilder, _LogRecordVOBuilder as _LogRecordVOBuilder, _EMPTY_SHELL_VO_BUILDER as _EMPTY_SHELL_VO_BUILDER, _DAMAGE_VALUE_VO_BUILDER as _DAMAGE_VALUE_VO_BUILDER, _VehicleVOBuilder as _VehicleVOBuilder, _DamageShellVOBuilder as _DamageShellVOBuilder, _ReceivedHitVehicleVOBuilder as _ReceivedHitVehicleVOBuilder, _CritsShellVOBuilder as _CritsShellVOBuilder, _CriticalHitValueVOBuilder as _CriticalHitValueVOBuilder, _ActionImgVOBuilder as _ActionImgVOBuilder, _AssistActionImgVOBuilder as _AssistActionImgVOBuilder, _ShellVOBuilder as _ShellVOBuilder, _ShellModeImgVOBuilder as _ShellModeImgVOBuilder
from gui.battle_control.battle_constants import PERSONAL_EFFICIENCY_TYPE as _ETYPE
from gui.impl.gen import R as R
from gui.Scaleform.genConsts.BATTLEDAMAGELOG_IMAGES import BATTLEDAMAGELOG_IMAGES as _IMAGES
from PlayerEvents import g_playerEvents as g_playerEvents
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from story_mode_common.story_mode_constants import VEHICLE_BUNKER_TURRET_TAG as VEHICLE_BUNKER_TURRET_TAG
_STORY_MODE_ETYPE_TO_RECORD_VO_BUILDER: dict

class StoryModeExtendedDamageActionVOBuilder(_DamageActionImgVOBuilder):
    def _getImage(self, info):
        ...

class StoryModeExtendedReceivedDamageActionVOBuilder(_DamageActionImgVOBuilder):
    def _getImage(self, info):
        ...

class StoryModeVehicleVOBuilder(_VehicleVOBuilder):
    sessionProvider: Any
    def _populateVO(self, vehicleVO, info, arenaDP):
        ...

class StoryModeReceivedHitVehicleVOBuilder(_ReceivedHitVehicleVOBuilder, StoryModeVehicleVOBuilder):
    ...

class _StoryModeLogViewComponent(_LogViewComponent):
    sessionProvider: Any
    _logViewMode: Any
    def updateViewMode(self, viewMode):
        ...
    def _buildLogMessageVO(self, info):
        ...

class StoryModeDamageLogPanel(DamageLogPanel):
    _topLog: Any
    _bottomLog: Any
    __vehStateCtrl: Any
    _isWinnerScreenShown: Any
    def __init__(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __onRoundFinished(self, winnerTeam, reason):
        ...
