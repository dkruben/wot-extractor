# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/uilogging/vehicle_mechanics/low_charge_shot/logger.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/vehicle_mechanics/low_charge_shot/logger.py
from __future__ import absolute_import
from uilogging.base.logger import MetricsLogger
from uilogging.constants import CommonLogActions
from uilogging.vehicle_mechanics.low_charge_shot.constants import FEATURE_LOW_CHARGE_SHOT, LOW_CHARGE_SHOT_SCREEN, LowChargeShotItems

class LowChargeShotUILogger(MetricsLogger):

    def __init__(self):
        super(LowChargeShotUILogger, self).__init__(FEATURE_LOW_CHARGE_SHOT)

    def onAlmostFinishedStarted(self):
        self.startAction(CommonLogActions.CLICK)

    def onAlmostFinishedEnded(self):
        self.reset()

    def onAlmostFinishedClicked(self, arenaUniqueID):
        self.stopAction(action=CommonLogActions.CLICK, item=LowChargeShotItems.AIMING_CIRCLE, info=str(arenaUniqueID), parentScreen=LOW_CHARGE_SHOT_SCREEN)
