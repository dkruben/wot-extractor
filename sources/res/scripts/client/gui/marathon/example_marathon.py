# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/marathon/example_marathon.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/marathon/example_marathon.py
from gui.impl.gen import R
from gui.marathon.marathon_event import MarathonEvent
from gui.marathon.marathon_event_container import MarathonEventContainer
from gui.marathon.marathon_event_controller import marathonCreator
from gui.Scaleform.locale.QUESTS import QUESTS

class ExampleMarathonEvent(MarathonEvent):

    @property
    def label(self):
        return R.strings.quests.missions.tab.label.may21_marathon()

    @property
    def tabTooltip(self):
        return QUESTS.MISSIONS_TAB_MAY21_MARATHON

    @property
    def entryTooltip(self):
        return self._data.tooltips

    @property
    def tokenPrefix(self):
        return self._data.tokenPrefix

    @property
    def grindPostfix(self):
        return self._data.grindPostfix

    @property
    def proPostfix(self):
        return self._data.proPostfix

    @property
    def finishedPostfix(self):
        return self._data.finishedPostfix

    @property
    def packagePrefix(self):
        return self._data.packagePrefix

    @property
    def packageTemplate(self):
        return self._data.packageTemplate

    @property
    def isNeedHandlingEscape(self):
        return True

    def createMarathonWebHandlers(self):
        from gui.marathon.web_handlers import createDefaultMarathonWebHandlers
        return createDefaultMarathonWebHandlers()


@marathonCreator(ExampleMarathonEvent)
class ExampleMarathon(MarathonEventContainer):

    def _override(self):
        self.prefix = 'may21_marathon'
        self.tokenPrefix = 'may21_marathon:KPZ07RH_'
        self.packagePrefix = 'KPZ07RH_'
        self.packageTemplate = 'kpz07rh_vehicle_{}0d{}'
        self.hangarFlagName = 'flag_may_marathon'
        self.grindPostfix = '_GRIND'
        self.proPostfix = '_PRO'
        self.finishedPostfix = '_v2'
        self.questsInChain = 10
        self.minVehicleLevel = 6
        self.questsPerStep = 3
