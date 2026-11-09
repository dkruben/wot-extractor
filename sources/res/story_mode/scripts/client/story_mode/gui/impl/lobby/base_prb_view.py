# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/impl/lobby/base_prb_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/impl/lobby/base_prb_view.py
from __future__ import absolute_import
from logging import getLogger
from adisp import adisp_process
from gui.impl.pub import ViewImpl
from gui.prb_control.dispatcher import g_prbLoader
from gui.prb_control.entities.base.ctx import PrbAction
from gui.prb_control.settings import PREBATTLE_ACTION_NAME
from helpers import dependency
from skeletons.gui.app_loader import IAppLoader
from story_mode.skeletons.story_mode_controller import IStoryModeController
from frameworks.wulf import ViewSettings, ViewFlags
from story_mode_common.story_mode_constants import LOGGER_NAME
_logger = getLogger(LOGGER_NAME)

class BasePrbView(ViewImpl):
    LAYOUT_ID = None
    MODEL_CLASS = None
    _storyModeCtrl = dependency.descriptor(IStoryModeController)
    _appLoader = dependency.descriptor(IAppLoader)

    def __init__(self, *_, **__):
        super(BasePrbView, self).__init__(settings=ViewSettings(layoutID=self.LAYOUT_ID, model=self.MODEL_CLASS(), flags=ViewFlags.LOBBY_SUB_VIEW))

    @adisp_process
    def _quit(self):
        prbDispatcher = g_prbLoader.getDispatcher()
        if prbDispatcher is not None:
            result = yield prbDispatcher.doSelectAction(PrbAction(PREBATTLE_ACTION_NAME.RANDOM))
            if not result:
                _logger.error('Failed to select random')
        return
