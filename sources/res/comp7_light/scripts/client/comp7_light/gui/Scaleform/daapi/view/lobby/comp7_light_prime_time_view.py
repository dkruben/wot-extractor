# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/Scaleform/daapi/view/lobby/comp7_light_prime_time_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/Scaleform/daapi/view/lobby/comp7_light_prime_time_view.py
from __future__ import absolute_import
from comp7_core.gui.Scaleform.daapi.view.lobby.comp7_core_prime_time_view import Comp7CorePrimeTimeView
from comp7_light.gui.comp7_light_constants import PREBATTLE_ACTION_NAME
from comp7_light.gui.impl.gen.view_models.views.lobby.enums import SeasonName
from gui.impl.gen import R
from helpers import dependency
from skeletons.gui.game_control import IComp7LightController

class Comp7LightPrimeTimeView(Comp7CorePrimeTimeView):
    _RES_STATUS_ROOT = R.strings.comp7_light.primeTimeView.status
    __comp7LightCtrl = dependency.descriptor(IComp7LightController)

    def _getController(self):
        return self.__comp7LightCtrl

    def _getPrbActionName(self):
        return PREBATTLE_ACTION_NAME.COMP7_LIGHT

    def _getPrbForcedActionName(self):
        return PREBATTLE_ACTION_NAME.COMP7_LIGHT

    @property
    def _seasonNameClazz(self):
        return SeasonName
