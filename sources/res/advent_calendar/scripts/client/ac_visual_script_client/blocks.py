# wot-extractor: codigo DESCOMPILADO de sources/res/advent_calendar/scripts/client/ac_visual_script_client/blocks.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: advent_calendar/scripts/client/ac_visual_script_client/blocks.py
from __future__ import absolute_import
from visual_script.block import Block, Meta
from visual_script.dependency import dependencyImporter
from visual_script import ASPECT
from visual_script.slot_types import SLOT_TYPE
event_dispatcher, dependency, game_controller, CurrentVehicle = dependencyImporter('advent_calendar.gui.shared.event_dispatcher', 'helpers.dependency', 'advent_calendar.skeletons.game_controller', 'CurrentVehicle')

class AdventCalendarMeta(Meta):

    @classmethod
    def blockColor(cls):
        return 10512127

    @classmethod
    def blockCategory(cls):
        return 'Advent'

    @classmethod
    def blockIcon(cls):
        return ':vse/blocks/arena'

    @classmethod
    def blockAspects(cls):
        return [ASPECT.HANGAR]


class OpenAdventCalendar(Block, AdventCalendarMeta):

    def __init__(self, *args, **kwargs):
        super(OpenAdventCalendar, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot('in', self._execute)
        self._out = self._makeEventOutputSlot('out')

    def _execute(self, *_):
        event_dispatcher.showAdventCalendarMainWindow()
        self._out.call()


class OnAdventCalendarConfigChanged(Block, AdventCalendarMeta):
    __adventController = dependency.descriptor(game_controller.IAdventCalendarController)

    def __init__(self, *args, **kwargs):
        super(OnAdventCalendarConfigChanged, self).__init__(*args, **kwargs)
        self._out = self._makeEventOutputSlot('out')

    def onStartScript(self):
        self.__adventController.onConfigChanged += self.__onConfigChanged

    def onFinishScript(self):
        self.__adventController.onConfigChanged -= self.__onConfigChanged

    def __onConfigChanged(self):
        self._out.call()


class IsAdventCalendarAvailable(Block, AdventCalendarMeta):
    __adventController = dependency.descriptor(game_controller.IAdventCalendarController)

    def __init__(self, *args, **kwargs):
        super(IsAdventCalendarAvailable, self).__init__(*args, **kwargs)
        self._isAvailable = self._makeDataOutputSlot('isAvailable', SLOT_TYPE.BOOL, self._execute)

    def _execute(self):
        self._isAvailable.setValue(self.__adventController.isAvailable())


class ADOnPreviewVehicleOrStyleSelected(Block, AdventCalendarMeta):

    def __init__(self, *args, **kwargs):
        super(ADOnPreviewVehicleOrStyleSelected, self).__init__(*args, **kwargs)
        self._out = self._makeEventOutputSlot('out')

    def onStartScript(self):
        CurrentVehicle.g_currentPreviewVehicle.onChanged += self.__onPreviewVehicleSelected

    def onFinishScript(self):
        CurrentVehicle.g_currentPreviewVehicle.onChanged -= self.__onPreviewVehicleSelected

    def __onPreviewVehicleSelected(self):
        self._out.call()


class ADIsPreviewVehicleOrStyleSelected(Block, AdventCalendarMeta):

    def __init__(self, *args, **kwargs):
        super(ADIsPreviewVehicleOrStyleSelected, self).__init__(*args, **kwargs)
        self._isSelected = self._makeDataOutputSlot('isSelected', SLOT_TYPE.BOOL, self._execute)

    def _execute(self):
        self._isSelected.setValue(CurrentVehicle.g_currentPreviewVehicle.item is not None)
        return
