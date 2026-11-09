# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/battle_results/templates.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/battle_results/templates.py
from __future__ import absolute_import
from gui.battle_results.components import base
from fort_rush.gui.battle_results import components as ex
from gui.battle_results.settings import BATTLE_RESULTS_RECORD as _RECORD
EXAMPLE_TOTAL_VO_META = base.DictMeta({'eventPoints': 0, 
   'vehicleCommanderID': 0, 
   'doubleTotalDamage': 0})
HB_TOTAL_RESULTS_BLOCK = base.StatsBlock(EXAMPLE_TOTAL_VO_META, 'victoryData')
HB_TOTAL_RESULTS_BLOCK.addNextComponent(ex.EventPointsItem('eventPoints', _RECORD.PERSONAL))
HB_TOTAL_RESULTS_BLOCK.addNextComponent(ex.VehicleCommanderIDItem('vehicleCommanderID', _RECORD.PERSONAL))
HB_TOTAL_RESULTS_BLOCK.addNextComponent(ex.VehicleDoubleDamage('doubleTotalDamage', _RECORD.PERSONAL))
