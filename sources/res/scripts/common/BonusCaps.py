# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/BonusCaps.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/BonusCaps.py
from __future__ import absolute_import
from typing import Dict, Optional, Set, FrozenSet

class BonusCapsConst(object):
    CONFIG_NAME = 'bonus_caps_override_config'
    REMOVE = 'remove'
    ADD = 'add'
    OVERRIDE = 'override'


class BonusCapsConfig(object):
    __slots__ = {
     '__config'}
    __OPERATIONS = {(BonusCapsConst.REMOVE): (lambda x, y: x - y), 
       (BonusCapsConst.ADD): (lambda x, y: x | y), 
       (BonusCapsConst.OVERRIDE): (lambda x, y: y)}

    def __init__(self, config=None):
        if not config:
            config = {}
        self.__config = config

    def __performOperations(self, arenaBonusType, defaultBonusCaps):
        configBonusCaps = self.__config[arenaBonusType]
        resultBonusCaps = set(defaultBonusCaps)
        for operation in configBonusCaps:
            resultBonusCaps = self.__OPERATIONS[operation](resultBonusCaps, configBonusCaps[operation])

        return resultBonusCaps

    def getModifiedBonusCaps(self, arenaBonusType, defaultBonusCaps):
        if self.__config.get(arenaBonusType, None) is None:
            return defaultBonusCaps
        else:
            return frozenset(self.__performOperations(arenaBonusType, defaultBonusCaps))
