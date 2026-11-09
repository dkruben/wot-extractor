# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/OwnVehicle.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/OwnVehicle.py
from __future__ import absolute_import
import logging, typing, BigWorld, BattleReplay
from OwnVehicleBase import OwnVehicleBase
if typing.TYPE_CHECKING:
    from Avatar import PlayerAvatar
_logger = logging.getLogger(__name__)

class OwnVehicle(OwnVehicleBase):

    def initialUpdate(self, force=False):
        super(OwnVehicle, self).initialUpdate(force=force)
        _logger.info('[%d] initialUpdate force=%s result=%s', self.entity.id, force, self.isInitialUpdated)

    def _avatar(self):
        avatar = BigWorld.player()
        if avatar.isObserver() and BattleReplay.isServerSideReplay():
            attachedVehicle = avatar.getVehicleAttached()
            if not attachedVehicle or attachedVehicle.id != self.entity.id:
                return None
        return avatar

    def _doLog(self, msg):
        _logger.debug(msg)

    def _serverTime(self):
        return BigWorld.serverTime()

    def _entities(self):
        return BigWorld.entities
