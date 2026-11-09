# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/game_loading/resources/cdn/consts.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_loading/resources/cdn/consts.py
import enum, typing
MAX_CONFIG_SEQUENCE_SLIDES_COUNT = 250
MAX_CONFIG_SEQUENCES_COUNT = 50
MIN_SLIDES_COUNT_TO_VIEW = 5
DOWNLOAD_SLIDES_MULTIPLAYER = 2
CDN_CACHE_SYNC_TIMEOUT = 300.0
NEWBIES_BATTLES_LIMIT = 400

@enum.unique
class SequenceOrders(str, enum.Enum):
    RANDOM = 'random'
    SUBSEQUENTLY = 'subsequently'


@enum.unique
class SequenceCohorts(str, enum.Enum):
    DEFAULT = 'default'
    NEWBIES = 'newbies'

    @classmethod
    def getDefaults(cls):
        return [
         cls.DEFAULT]
