# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/battle/sixth_sence_indicator.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/battle/sixth_sence_indicator.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.battle.shared.indicators import SixthSenseIndicator
from helpers.dependency import descriptor
from skeletons.gui.battle_session import IBattleSessionProvider

class StoryModeSixthSenseIndicator(SixthSenseIndicator):
    __session = descriptor(IBattleSessionProvider)

    def _isSixthSenseEnabled(self):
        vehicle = self.__session.shared.vehicleState.getControllingVehicle()
        enabled = vehicle and 'SMDetectionDelayObservableComponent' not in vehicle.dynamicComponents
        return enabled
