# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/gui_items/processors/player_satisfaction_rating.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/gui_items/processors/player_satisfaction_rating.py
from __future__ import absolute_import
import BigWorld
from gui.shared.gui_items.processors import Processor

class PlayerSatisfactionRatingProcessor(Processor):

    def __init__(self, arenaUniqueID, rating):
        super(PlayerSatisfactionRatingProcessor, self).__init__()
        self._arenaUniqueID = arenaUniqueID
        self._rating = rating

    def _request(self, callback):
        BigWorld.player().submitPlayerSatisfactionRating(self._arenaUniqueID, self._rating, (lambda code, errStr: self._response(code, callback, errStr=errStr)))
