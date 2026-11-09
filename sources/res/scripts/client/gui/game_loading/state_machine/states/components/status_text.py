# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/game_loading/state_machine/states/components/status_text.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_loading/state_machine/states/components/status_text.py
import typing, game_loading_bindings
from frameworks_common.state_machine import StateFlags, StateEvent
from gui.game_loading import loggers
from gui.game_loading.resources.consts import MilestonesTypes, Milestones
from gui.game_loading.state_machine.const import TickingMode
from gui.game_loading.state_machine.models import LoadingMilestoneModel
from gui.game_loading.state_machine.states.base import BaseViewResourcesTickingState, BaseTickingState
from gui.game_loading.state_machine.states.handlers.milestones import StatusTextMilestonesHandler
if typing.TYPE_CHECKING:
    from gui.game_loading.resources.models import StatusTextModel
_logger = loggers.getStatesLogger()

class StatusTextStateComponent(BaseViewResourcesTickingState):
    __slots__ = ()

    def _view(self, resource):
        game_loading_bindings.setStatusText(resource.text)


class MilestoneStatusTextStateComponent(BaseTickingState):
    __slots__ = ('_milestonesHandler', '_milestone', '_retainMilestones')

    def __init__(self, stateID, milestonesSettings, flags=StateFlags.UNDEFINED, tickingMode=TickingMode.MANUAL, onCompleteEvent=None):
        super(MilestoneStatusTextStateComponent, self).__init__(stateID=stateID, flags=flags, tickingMode=tickingMode, onCompleteEvent=onCompleteEvent)
        self._milestonesHandler = StatusTextMilestonesHandler(milestonesSettings=milestonesSettings)
        self._milestone = self._milestonesHandler.getCurrentMilestone()
        self._retainMilestones = False
        _logger.debug('[%s] Apply default milestone: %s. Status: %s.', self, self._milestone.name, self._milestone.status.text)

    def setRetainMilestones(self, value):
        self._retainMilestones = value

    def _start(self):
        self._milestonesHandler.onMilestoneReached += self._onMilestoneReached
        self._milestonesHandler.onMilestoneTypeChanged += self._onMilestoneTypeChanged
        if not self._retainMilestones:
            self._milestone = None
            self._milestonesHandler.chooseDefaultMilestoneType()
        elif self._milestone is not None:
            self._onMilestoneReached(self._milestone)
        self._milestonesHandler.start()
        super(MilestoneStatusTextStateComponent, self)._start()
        return

    def _stop(self):
        super(MilestoneStatusTextStateComponent, self)._stop()
        self._milestonesHandler.stop()
        self._milestonesHandler.onMilestoneReached -= self._onMilestoneReached
        self._milestonesHandler.onMilestoneTypeChanged -= self._onMilestoneTypeChanged

    def _onMilestoneReached(self, newMilestone):
        _logger.debug('[%s] Milestone reached: %s. New text status:  %s.', self, newMilestone.name, newMilestone.status.text)
        self._milestone = newMilestone
        if newMilestone.forceApply:
            self._setStatus(newMilestone.status.text)

    def _onMilestoneTypeChanged(self, newMilestone):
        _logger.debug('[%s] Milestone type changed: %s. New text status:  %s.', self, newMilestone.name, newMilestone.status.text)
        self._milestone = newMilestone

    def _task(self):
        self._setStatus(self._milestone.status.text)
        return self._milestone.status.minShowTimeSec

    @staticmethod
    def _setStatus(newStatus):
        if newStatus:
            game_loading_bindings.setStatusText(newStatus)
