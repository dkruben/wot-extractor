# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/dog_tags_common/settings_constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/dog_tags_common/settings_constants.py
from __future__ import absolute_import
from enum import Enum
DT_PDATA_KEY = 'dogTags'

class Settings(Enum):
    SHOW_VICTIMS_DT = 'showVictimsDogTag'
    SHOW_DT_TO_KILLER = 'showDogTagToKiller'

    def __lt__(self, other):
        return self.value < other.value


SETTINGS_POSITIONS = {(Settings.SHOW_VICTIMS_DT): 1, 
   (Settings.SHOW_DT_TO_KILLER): 2}
