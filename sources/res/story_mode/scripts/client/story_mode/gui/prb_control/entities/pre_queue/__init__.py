# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/prb_control/entities/pre_queue/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/prb_control/entities/pre_queue/__init__.py
from __future__ import absolute_import
from adisp import adisp_process, adisp_async
import wg_async as future_async
from gui.impl.dialogs import dialogs
from gui.impl.dialogs.builders import WarningDialogBuilder
from gui.impl.gen import R
from helpers import dependency
from story_mode.skeletons.story_mode_controller import IStoryModeController
from story_mode.uilogging.story_mode.consts import LogButtons
from story_mode.uilogging.story_mode.loggers import TasksCompletedWarningLogger

@adisp_async
@future_async.wg_async
def checkTasksAvailable(callback):
    ctrl = dependency.instance(IStoryModeController)
    mission = ctrl.missions.getMission(ctrl.selectedMissionId)
    if mission and all(ctrl.isMissionTaskCompleted(mission.missionId, task.id) for task in mission.getUnlockedTasks()):
        logger = TasksCompletedWarningLogger()
        logger.logOpen(state=str(ctrl.selectedMissionId))
        builder = WarningDialogBuilder()
        rMsg = R.strings.sm_lobby.dialogs.missionCompleted
        builder.setMessagesAndButtons(rMsg, rMsg)
        builder.setShowBalance(True)
        success = yield future_async.wg_await(dialogs.showSimple(builder.buildInLobby()))
        if success:
            logger.logClick(LogButtons.SUBMIT, state=str(ctrl.selectedMissionId))
        else:
            logger.logClick(LogButtons.QUIT, state=str(ctrl.selectedMissionId))
        callback(success)
    else:
        callback(True)


def tasksAvailableCheck(func):

    @adisp_process
    def wrapper(*args, **kwargs):
        res = yield checkTasksAvailable()
        if res:
            func(*args, **kwargs)
        elif kwargs.get('callback') is not None:
            kwargs.get('callback')(False)
        return

    return wrapper
