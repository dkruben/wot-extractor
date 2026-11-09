# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client_common/script_component/ScriptComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client_common/script_component/ScriptComponent.py
from __future__ import absolute_import
import logging, BigWorld, Avatar
from PlayerEvents import g_playerEvents
from helpers import dependency, isPlayerAvatar
from shared_utils import nextTick
from skeletons.gui.battle_session import IBattleSessionProvider
_logger = logging.getLogger(__name__)

class ScriptComponent(BigWorld.StaticScriptComponent):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)
    REQUIRED_BONUS_CAP = None

    def __init__(self):
        BigWorld.StaticScriptComponent.__init__(self)
        if not self.__checkBonusCaps():
            return
        if self._isAvatarReady:
            nextTick(self._onAvatarReady)()
        else:
            g_playerEvents.onAvatarReady += self.__onAvatarReady

    @property
    def _isAvatarReady(self):
        return isPlayerAvatar() and BigWorld.player().userSeesWorld()

    def onEnterWorld(self, _):
        _logger.debug('%s.onEnterWorld. EntityID=%s', self.__class__.__name__, self.entity.id)

    def onLeaveWorld(self):
        _logger.debug('%s.onLeaveWorld. EntityID=%s', self.__class__.__name__, self.entity.id)

    def _onAvatarReady(self):
        pass

    def __onAvatarReady(self):
        g_playerEvents.onAvatarReady -= self.__onAvatarReady
        self._onAvatarReady()

    def __checkBonusCaps(self):
        if self.REQUIRED_BONUS_CAP is None:
            return True
        else:
            if isinstance(self.entity, Avatar.PlayerAvatar):
                capsChecker = self.entity.hasBonusCap
            else:
                capsChecker = self.__sessionProvider.arenaVisitor.bonus.hasBonusCap
            return capsChecker(self.REQUIRED_BONUS_CAP)
