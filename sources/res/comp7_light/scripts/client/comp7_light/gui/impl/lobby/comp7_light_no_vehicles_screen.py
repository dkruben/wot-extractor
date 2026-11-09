# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/comp7_light_no_vehicles_screen.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/impl/lobby/comp7_light_no_vehicles_screen.py
from __future__ import absolute_import
from comp7_core.gui.impl.lobby.no_vehicles_screen import NoVehiclesScreen
from comp7_light.gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as COMP7_LIGHT_TOOLTIPS
from comp7_light.gui.impl.gen.view_models.views.lobby.enums import SeasonName
from comp7_light.gui.impl.gen.view_models.views.lobby.no_vehicles_screen_model import ErrorReason
from comp7_light.gui.impl.gen.view_models.views.lobby.no_vehicles_screen_model import NoVehiclesScreenModel
from comp7_light.gui.impl.gen.view_models.views.lobby.season_model import SeasonState
from comp7_light.gui.impl.gen.view_models.views.lobby.year_model import YearState
from helpers import dependency
from skeletons.gui.game_control import IComp7LightController

class Comp7LightNoVehiclesScreen(NoVehiclesScreen):
    __comp7LightController = dependency.descriptor(IComp7LightController)

    @property
    def _modeController(self):
        return self.__comp7LightController

    @property
    def _modelClazz(self):
        return NoVehiclesScreenModel

    @property
    def _seasonStateClazz(self):
        return SeasonState

    @property
    def _yearStateClazz(self):
        return YearState

    @property
    def _errorReasonClazz(self):
        return ErrorReason

    @property
    def _seasonNameClazz(self):
        return SeasonName

    @property
    def _calendarDayTooltipID(self):
        return COMP7_LIGHT_TOOLTIPS.COMP7_LIGHT_CALENDAR_DAY_INFO
