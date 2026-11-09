# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/common/comp7_common/comp7_battle_results/comp7.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/common/comp7_common/comp7_battle_results/comp7.py
from __future__ import absolute_import
from battle_results.battle_results_constants import BATTLE_RESULT_ENTRY_TYPE as ENTRY_TYPE
from comp7_core_common.battle_results.comp7_core import BATTLE_RESULTS as COMP7_BATTLE_RESULTS
BATTLE_RESULTS = COMP7_BATTLE_RESULTS + [
 (
  'comp7Rating', int, 0, None, 'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  'comp7Rank', tuple, (0, 0, 0), None, 'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  'comp7RatingDelta', int, 0, None, 'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  'comp7TeamStats', dict, {}, None, 'skip', ENTRY_TYPE.SERVER),
 (
  'comp7QualActive', None, None, None, 'skip', ENTRY_TYPE.ACCOUNT_ALL),
 (
  'comp7QualBattleIndex', int, 0, None, 'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  'comp7QualRating', int, 0, None, 'skip', ENTRY_TYPE.SERVER),
 (
  'comp7QualRank', tuple, (0, 0), None, 'skip', ENTRY_TYPE.SERVER)]
