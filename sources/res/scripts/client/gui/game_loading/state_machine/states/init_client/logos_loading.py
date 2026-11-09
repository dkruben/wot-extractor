# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/game_loading/state_machine/states/init_client/logos_loading.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_loading/state_machine/states/init_client/logos_loading.py
import typing, game_loading_bindings
from frameworks_common.state_machine import StringEvent, StateFlags
from gui.game_loading import loggers
from gui.game_loading.state_machine.const import GameLoadingStates, GameLoadingStatesEvents, TickingMode
from gui.game_loading.state_machine.states.base import BaseViewResourcesTickingState
from gui.impl import backport
from gui.impl.gen import R
from helpers import getFullClientVersion
if typing.TYPE_CHECKING:
    from gui.game_loading.resources.models import LogoModel, LocalImageModel
    from gui.game_loading.resources.local.base import LocalResources
_logger = loggers.getStatesLogger()

class LogosLoadingState(BaseViewResourcesTickingState):
    __slots__ = ('_ageRatingPath', )

    def __init__(self, logos, ageRatingPath):
        super(LogosLoadingState, self).__init__(stateID=GameLoadingStates.CLIENT_INIT_LOGOS.value, resources=logos, flags=StateFlags.INITIAL, tickingMode=TickingMode.BOTH, onCompleteEvent=StringEvent(GameLoadingStatesEvents.LOGOS_SHOWN.value))
        self._ageRatingPath = ageRatingPath

    @property
    def lastShownImage(self):
        return

    def _view(self, resource):
        if not game_loading_bindings.isViewOpened():
            _logger.debug('[%s] opening GF view.', self)
            game_loading_bindings.createLoadingView()
        data = {'version': (getFullClientVersion() if resource.showVersion else ''), 
           'copyright': (backport.text(R.strings.menu.copy()) if resource.showCopyright else ''), 
           'logoType': (resource.type), 
           'transitionTime': (resource.transition), 
           'info': (resource.info), 
           'infoStyle': (resource.infoStyle.value), 
           'ageRatingPath': (self._ageRatingPath)}
        game_loading_bindings.setViewData(data)
        _logger.debug('[%s] image [%s] shown.', self, resource)
