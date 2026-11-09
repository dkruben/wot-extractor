# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_control/controllers/appearance_cache_ctrls/maps_training_appearance_cache_ctrl.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/appearance_cache_ctrls/maps_training_appearance_cache_ctrl.py
from __future__ import absolute_import
import logging
from gui.battle_control.controllers.appearance_cache_ctrls.event_appearance_cache_ctrl import EventAppearanceCacheController
from helpers import uniprof
_logger = logging.getLogger(__name__)

class MapsTrainingAppearanceCacheController(EventAppearanceCacheController):

    @uniprof.regionDecorator(label='MapsTrainingAppearanceCacheController.updateSpawnList', scope='wrap')
    def updateSpawnList(self, spawnListData):
        self._updateSpawnList(spawnListData)
        _logger.debug('MapsTrainingAppearanceCacheController SpawnList cache updated=%s', spawnListData)
