# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/common/player_satisfaction_rating/player_satisfaction_sound.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/common/player_satisfaction_rating/player_satisfaction_sound.py
from __future__ import absolute_import
import logging
from enum import Enum
import SoundGroups
from constants import PlayerSatisfactionRating
_logger = logging.getLogger(__name__)

class SoundEvents(Enum):
    BETTER = 'post_battle_voting_better'
    USUAL = 'post_battle_voting_usual'
    WORSE = 'post_battle_voting_worse'


_RATING_TO_SOUND_MAP = {(PlayerSatisfactionRating.USUAL): (SoundEvents.USUAL), 
   (PlayerSatisfactionRating.BETTER): (SoundEvents.BETTER), 
   (PlayerSatisfactionRating.WORSE): (SoundEvents.WORSE)}

def playSoundForRating(rating):
    SoundGroups.g_instance.playSound2D(_RATING_TO_SOUND_MAP[rating].value)
