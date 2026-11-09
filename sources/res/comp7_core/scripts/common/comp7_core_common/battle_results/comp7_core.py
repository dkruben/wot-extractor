# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_core/scripts/common/comp7_core_common/battle_results/comp7_core.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_core/scripts/common/comp7_core_common/battle_results/comp7_core.py
from __future__ import absolute_import
from battle_results.battle_results_constants import BATTLE_RESULT_ENTRY_TYPE as ENTRY_TYPE
BATTLE_RESULTS = [
 (
  'comp7PrestigePoints', int, 0, None, 'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  'roleSkillUsed', int, 0, None, 'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  'healthRepair', int, 0, None, 'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  'alliedHealthRepair', int, 0, None, 'sum', ENTRY_TYPE.VEHICLE_ALL),
 (
  'fareTeamPrestigePointsPosition', int, 0, None, 'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  'isSuperSquad', bool, False, None, 'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  'comp7BannedVehicles', dict, {}, None, 'skip', ENTRY_TYPE.COMMON)]
