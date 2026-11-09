# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/battle_results/comp7_light_team_stats_params_settings.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/impl/lobby/battle_results/comp7_light_team_stats_params_settings.py
from __future__ import absolute_import
import typing
from gui.battle_results.presenters.packers.team.stats_params_settings import _Parameter
from comp7_light.gui.impl.gen.view_models.views.lobby.battle_results import comp7_light_detailed_stats_parameter_model
from constants import EntityCaptured
from gui.battle_results.pbs_helpers.team_stats_helpers import getStatsParamValue
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.battle_results.simple_stats_parameter_model import ValueType, RegularParamType
if typing.TYPE_CHECKING:
    from comp7_core.gui.battle_results.reusable.shared import Comp7CoreVehicleSummarizeInfo

def getPoiCapturable(summarizeInfo, fields, _):
    return (getattr(summarizeInfo, field).get(EntityCaptured.POI_CAPTURABLE, 0) for field in fields)


COMP7_LIGHT_PARAMETERS_UPDATE = {(RegularParamType.DAMAGEDEALT): (_Parameter(path=R.strings.battle_results.team.stats.parameter.damageDealt, stringId='damageDealt', fields=('damageDealt', ), valueType=ValueType.INTEGER, conditions=None, extractor=getStatsParamValue, details=(
                                  RegularParamType.SNIPERDAMAGEDEALT,
                                  RegularParamType.ARTILLERYSTRIKE,
                                  comp7_light_detailed_stats_parameter_model.Comp7LightParamType.DAMAGEDEALTBYSKILLS))), 
   (comp7_light_detailed_stats_parameter_model.Comp7LightParamType.DAMAGEDEALTBYSKILLS): (_Parameter(path=R.strings.battle_results.team.stats.labels_damageDealtBySkills, stringId='damageDealtBySkills', fields=('equipmentDamageDealt', ), valueType=ValueType.INTEGER, conditions=None, extractor=getStatsParamValue, details=())), 
   (comp7_light_detailed_stats_parameter_model.Comp7LightParamType.HEALED): (_Parameter(path=R.strings.battle_results.team.stats.labels_healed, stringId='healed', fields=('healthRepair',
                                                                                               'alliedHealthRepair'), valueType=ValueType.INTEGER, conditions=None, extractor=getStatsParamValue, details=())), 
   (comp7_light_detailed_stats_parameter_model.Comp7LightParamType.CAPTUREDPOINTSOFINTEREST): (_Parameter(path=R.strings.battle_results.team.stats.labels_capturedPointsOfInterest, stringId='capturedPointsOfInterest', fields=('entityCaptured', ), valueType=ValueType.INTEGER, conditions=None, extractor=getPoiCapturable, details=())), 
   (comp7_light_detailed_stats_parameter_model.Comp7LightParamType.ROLESKILLUSED): (_Parameter(path=R.strings.battle_results.team.stats.labels_roleSkillUsed, stringId='roleSkillUsed', fields=('roleSkillUsed', ), valueType=ValueType.INTEGER, conditions=None, extractor=getStatsParamValue, details=()))}
