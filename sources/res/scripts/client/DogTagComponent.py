# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/DogTagComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/DogTagComponent.py
from __future__ import absolute_import
import logging, BigWorld
_logger = logging.getLogger(__name__)

class DogTagComponent(BigWorld.DynamicScriptComponent):

    def set_killerDogTag(self, old):
        if self._isObserving():
            return
        else:
            _logger.info('DogTagComponent.set_killerDogTag: killerDogTag %s', str(self.killerDogTag))
            dogTagsCtrl = self.entity.guiSessionProvider.dynamic.dogTags
            if dogTagsCtrl is not None:
                dogTagsCtrl.setKillerDogTag(self.killerDogTag)
            return

    def setSlice_victimsDogTags(self, changePath, oldValue):
        if self._isObserving():
            return
        else:
            _logger.info('DogTagComponent.setSlice_victimsDogTags: victimsDogTags %s, changePath %s', str(self.victimsDogTags), str(changePath))
            dogTagsCtrl = self.entity.guiSessionProvider.dynamic.dogTags
            if dogTagsCtrl is not None:
                begin, end = changePath[0]
                newVictimsDogTags = self.victimsDogTags[begin:end]
                dogTagsCtrl.setVictimsDogTags(newVictimsDogTags)
            return

    @staticmethod
    def _isObserving():
        player_vehicle = BigWorld.player().getVehicleAttached()
        if player_vehicle is not None:
            return not player_vehicle.isPlayerVehicle
        else:
            return False
