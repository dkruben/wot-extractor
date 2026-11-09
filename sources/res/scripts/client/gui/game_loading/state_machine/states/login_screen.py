# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/game_loading/state_machine/states/login_screen.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_loading/state_machine/states/login_screen.py
import typing, game_loading_bindings
from frameworks_common.state_machine import StateFlags
from gui.game_loading.state_machine.const import GameLoadingStates
from gui.game_loading.state_machine.models import ImageViewSettingsModel
from gui.game_loading.state_machine.states.slide import StaticSlideState
if typing.TYPE_CHECKING:
    from gui.game_loading.resources.cdn.images import CdnImagesResources

class LoginScreenState(StaticSlideState):
    __slots__ = ('_nextSlideDuration', )

    def __init__(self, images, nextSlideDuration, viewSettings):
        super(LoginScreenState, self).__init__(stateID=GameLoadingStates.LOGIN_SCREEN.value, flags=StateFlags.UNDEFINED, images=images, imageViewSettings=viewSettings)
        self._nextSlideDuration = nextSlideDuration

    @property
    def nextSlideDuration(self):
        return self._nextSlideDuration

    def _onEntered(self, event):
        super(LoginScreenState, self)._onEntered(event)
        game_loading_bindings.bringLoadingViewToBottom()
