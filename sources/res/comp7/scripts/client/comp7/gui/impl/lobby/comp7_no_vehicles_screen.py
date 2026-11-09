# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/comp7_no_vehicles_screen.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/lobby/comp7_no_vehicles_screen.py
from __future__ import absolute_import
from comp7.gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as COMP7_TOOLTIPS
from comp7.gui.impl.gen.view_models.views.lobby.enums import SeasonName
from comp7.gui.impl.gen.view_models.views.lobby.no_vehicles_screen_model import ErrorReason
from comp7.gui.impl.gen.view_models.views.lobby.no_vehicles_screen_model import NoVehiclesScreenModel
from comp7.gui.impl.gen.view_models.views.lobby.season_model import SeasonState
from comp7.gui.impl.gen.view_models.views.lobby.year_model import YearState
from comp7_core.gui.impl.lobby.no_vehicles_screen import NoVehiclesScreen
from helpers import dependency
from skeletons.gui.game_control import IComp7Controller

class Comp7NoVehiclesScreen(NoVehiclesScreen):
    __comp7Controller = dependency.descriptor(IComp7Controller)

    @property
    def _modeController(self):
        return self.__comp7Controller

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
        return COMP7_TOOLTIPS.COMP7_CALENDAR_DAY_INFO
