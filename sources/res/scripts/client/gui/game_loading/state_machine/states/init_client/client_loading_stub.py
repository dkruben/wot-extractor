# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/game_loading/state_machine/states/init_client/client_loading_stub.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_loading/state_machine/states/init_client/client_loading_stub.py
import typing, BigWorld, game_loading_bindings
from shared_utils import safeCancelCallback
from helpers.time_utils import MS_IN_SECOND
from gui.game_loading import loggers
from gui.game_loading.state_machine.const import GameLoadingStates
from gui.game_loading.state_machine.models import ImageViewSettingsModel
from gui.game_loading.state_machine.states.slide import StaticSlideState
if typing.TYPE_CHECKING:
    from gui.game_loading.resources.cdn.images import CdnImagesResources
_logger = loggers.getStatesLogger()

class ClientLoadingStubState(StaticSlideState):
    __slots__ = ('_minDurationTimerId', )

    def __init__(self, images):
        super(ClientLoadingStubState, self).__init__(GameLoadingStates.CLIENT_INIT_LOADING_STUB.value, images, ImageViewSettingsModel(showSmallLogo=False, showVfx=False))
        self._minDurationTimerId = None
        return

    def clear(self):
        self._cancelMinDurationTimer()
        super(ClientLoadingStubState, self).clear()

    def _onEntered(self, event):
        super(ClientLoadingStubState, self)._onEntered(event)
        game_loading_bindings.bringLoadingViewToTop()
        self._minDurationTimerId = BigWorld.callback(self._image.transition / float(MS_IN_SECOND), self._fireMinimumDurationEvent)

    def _onExited(self):
        self._cancelMinDurationTimer()
        super(ClientLoadingStubState, self)._onExited()

    def _fireMinimumDurationEvent(self):
        self._cancelMinDurationTimer()
        self._releaseWaiting()

    def _cancelMinDurationTimer(self):
        if self._minDurationTimerId is not None:
            safeCancelCallback(self._minDurationTimerId)
            self._minDurationTimerId = None
        return
