# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/battle_results/battle_royale.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/battle_results/battle_royale.py
from __future__ import absolute_import
from battle_results.battle_results_constants import BATTLE_RESULT_ENTRY_TYPE as ENTRY_TYPE
from DictPackers import ValueReplayPacker, MergeDictPacker
BATTLE_RESULTS = [
 (
  'maxAchievedBRTitle', tuple, (0, 0), None, 'skip', ENTRY_TYPE.ACCOUNT_SELF),
 (
  'brPosInBattle', int, 255, None, 'skip', ENTRY_TYPE.VEHICLE_SELF),
 (
  'battleXPTotal', int, 0, None, 'sum', ENTRY_TYPE.SERVER),
 (
  'modulesDescriptors', list, [], None, 'extend', ENTRY_TYPE.SERVER),
 (
  'achivedLevel', int, 1, None, 'skip', ENTRY_TYPE.VEHICLE_ALL),
 (
  'brAwardTokens', dict, {}, None, 'joinDicts', ENTRY_TYPE.ACCOUNT_SELF),
 (
  'currencies', dict, {},
  MergeDictPacker((
   'brcoin', dict, {},
   MergeDictPacker((
    'count', int, 0, None, 'sum'), (
    'original', int, 0, None, 'sum'), (
    'replay', str, '', ValueReplayPacker(), 'skip'), (
    'premiumFactor100', int, 0, None, 'any'), (
    'premiumPlusFactor100', int, 0, None, 'any'), (
    'premiumVipFactor100', int, 0, None, 'any'), (
    'appliedPremiumFactor100', int, 0, None, 'any'), (
    'coinsForPlace', int, 0, None, 'any'), (
    'dailyBonusFactor', int, 0, None, 'any'), (
    'leaveCoins', int, 0, None, 'any'), (
    'subtotal', int, 0, None, 'sum')),
   'joinByEachPacker'), (
   'stpcoin', dict, {},
   MergeDictPacker((
    'count', int, 0, None, 'sum'), (
    'original', int, 0, None, 'sum'), (
    'replay', str, '', ValueReplayPacker(), 'skip'), (
    'premiumFactor100', int, 0, None, 'any'), (
    'premiumPlusFactor100', int, 0, None, 'any'), (
    'premiumVipFactor100', int, 0, None, 'any'), (
    'appliedPremiumFactor100', int, 0, None, 'any'), (
    'coinsForPlace', int, 0, None, 'any'), (
    'dailyBonusFactor', int, 0, None, 'any'), (
    'leaveCoins', int, 0, None, 'any'), (
    'subtotal', int, 0, None, 'sum')),
   'joinByEachPacker')),
  'joinByEachPacker', ENTRY_TYPE.VEHICLE_SELF)]
