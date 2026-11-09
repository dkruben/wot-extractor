# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/items/perks.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/items/perks.py
from __future__ import absolute_import
from constants import ITEM_DEFS_PATH
from items.readers.perks_readers import readPerksCacheFromXML
from items.components.perks_components import PerksCashe
_PERK_XML_PATH = ITEM_DEFS_PATH + 'perks/'
g_cache = None

def init(preloadEverything):
    global g_cache
    g_cache = Cache()
    if preloadEverything:
        g_cache.initPerks()


class Cache(object):
    __slots__ = ('__perks', )

    def __init__(self):
        self.__perks = None
        return

    def initPerks(self):
        if self.__perks is None:
            self.__perks = PerksCashe()
            readPerksCacheFromXML(self.__perks, _PERK_XML_PATH)
        return

    @property
    def perks(self):
        if self.__perks is None:
            self.initPerks()
        return self.__perks
