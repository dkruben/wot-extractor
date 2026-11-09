# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/battle_results/tooltips/total_efficiency_tooltips.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/battle_results/tooltips/total_efficiency_tooltips.py
from __future__ import absolute_import
import typing
from gui.battle_results.presenters.packers.tooltips.efficiency_tooltips import KillsParameter, StunParameter, SpottedParameter, DefencePointsParameter, DamageDealtParameter, DamageAssistedParameter, DamageBlockedByArmorParameter, CapturePointsParameter, EfficiencyTooltipsPacker
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.battle_results.efficiency_param_constants import EfficiencyParamConstants
from soft_exception import SoftException
if typing.TYPE_CHECKING:
    from gui.battle_results.stats_ctrl import BattleResults
    from gui.impl.gen.view_models.views.lobby.battle_results.tooltips.efficiency_tooltip_model import EfficiencyTooltipModel
_STR_PATH = R.strings.fun_battle_results.efficiencyTooltip.header

class FunTotalKillsParameter(KillsParameter):
    _TITLE = _STR_PATH.kills


class FunTotalDamageDealtParameter(DamageDealtParameter):
    _TITLE = _STR_PATH.damageDealt


class FunTotalStunParameter(StunParameter):
    _TITLE = _STR_PATH.damageAssistedStun


class FunTotalDamageBlockedByArmorParameter(DamageBlockedByArmorParameter):
    _TITLE = _STR_PATH.damageBlockedByArmor


class FunTotalDamageAssistedParameter(DamageAssistedParameter):
    _TITLE = _STR_PATH.damageAssisted


class FunTotalSpottedParameter(SpottedParameter):
    _TITLE = _STR_PATH.spotted


class FunTotalCapturePointsParameter(CapturePointsParameter):
    _TITLE = _STR_PATH.capturePoints


class FunTotalDefencePointsParameter(DefencePointsParameter):
    _TITLE = _STR_PATH.droppedCapturePoints


_FUN_PARAMETERS_TO_TOOLTIP_MAP = {(EfficiencyParamConstants.STUN): FunTotalStunParameter, 
   (EfficiencyParamConstants.DAMAGE_DEALT): FunTotalDamageDealtParameter, 
   (EfficiencyParamConstants.DAMAGE_BLOCKED_BY_ARMOR): FunTotalDamageBlockedByArmorParameter, 
   (EfficiencyParamConstants.DAMAGE_ASSISTED): FunTotalDamageAssistedParameter, 
   (EfficiencyParamConstants.SPOTTED): FunTotalSpottedParameter, 
   (EfficiencyParamConstants.KILLS): FunTotalKillsParameter, 
   (EfficiencyParamConstants.CAPTURE_POINTS): FunTotalCapturePointsParameter, 
   (EfficiencyParamConstants.DROPPED_CAPTURE_POINTS): FunTotalDefencePointsParameter}

class FunEfficiencyTooltipsPacker(EfficiencyTooltipsPacker):
    _TOOLTIPS = _FUN_PARAMETERS_TO_TOOLTIP_MAP

    @classmethod
    def packTooltip(cls, model, battleResults, ctx=None):
        if not ctx['paramType']:
            raise SoftException('Missing parameter type for the FunEfficiencyTooltip')
        ctx['isZeroValuesVisible'] = True
        ctx['isAdditionalValuesVisible'] = False
        super(FunEfficiencyTooltipsPacker, cls).packTooltip(model, battleResults, ctx)
