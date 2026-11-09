# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client_common/script_component/DynamicScriptComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client_common/script_component/DynamicScriptComponent.py
from __future__ import absolute_import
import logging
from future.utils import iteritems
import BigWorld
from PlayerEvents import g_playerEvents
from shared_utils import nextTick
from vehicle_systems.stricted_loading import makeCallbackWeak
_logger = logging.getLogger(__name__)

class DynamicScriptComponent(BigWorld.DynamicScriptComponent):

    def __init__(self, *_, **__):
        BigWorld.DynamicScriptComponent.__init__(self)
        if self._isAvatarReady:
            nextTick(makeCallbackWeak(self.__onAvatarReady))()
        else:
            g_playerEvents.onAvatarReady += self.__onAvatarReady
        _logger.debug('%s.__init__. EntityID=%s', self.__class__.__name__, self.entity.id)

    @property
    def _isAvatarReady(self):
        return BigWorld.player().userSeesWorld()

    def onDestroy(self):
        _logger.debug('%s.onDestroy. EntityID=%s', self.__class__.__name__, self.entity.id)
        g_playerEvents.onAvatarReady -= self.__onAvatarReady

    def onLeaveWorld(self):
        self.onDestroy()

    @property
    def spaceID(self):
        return self.entity.spaceID

    @property
    def keyName(self):
        return next(name for name, value in iteritems(self.entity.dynamicComponents) if value == self)

    def _onAvatarReady(self):
        pass

    def __onAvatarReady(self):
        g_playerEvents.onAvatarReady -= self.__onAvatarReady
        if self._isValid:
            self._onAvatarReady()

    @property
    def _isValid(self):
        return not self.entity.isDestroyed and self in self.entity.dynamicComponents.values()
