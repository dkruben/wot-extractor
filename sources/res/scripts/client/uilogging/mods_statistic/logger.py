# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/uilogging/mods_statistic/logger.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/mods_statistic/logger.py
from __future__ import absolute_import
import json, logging
from future.utils import iteritems
import BigWorld
from uilogging.base.logger import _BaseLogger as Logger
from uilogging.constants import DEFAULT_LOGGER_NAME
from wotdecorators import noexcept
_logger = logging.getLogger(DEFAULT_LOGGER_NAME)

class ModsStatisticLogger(Logger):
    FEATURE_NAME = 'mods_statistic'
    GROUP_NAME = 'mods_statistic'
    ACTION = 'collected'
    MAX_JSON_STR_LEN = 10000
    MD5_LEN = 32
    __alreadyLogged = False

    def __init__(self):
        super(ModsStatisticLogger, self).__init__(self.FEATURE_NAME, self.GROUP_NAME)

    @noexcept
    def log(self):
        if ModsStatisticLogger.__alreadyLogged:
            return
        _logger.debug('Mods statistic requested.')
        if self.disabled:
            return
        mods = BigWorld.wg_getMods()
        if not mods:
            _logger.debug('There are not mods.')
            return
        jsonStrLen = 2
        tmpMods = {}
        for modName, md5 in iteritems(mods):
            rowStrLen = 0
            rowStrLen += 5 + self.MD5_LEN
            rowStrLen += len(modName)
            if jsonStrLen + rowStrLen <= self.MAX_JSON_STR_LEN:
                tmpMods[modName] = md5
                jsonStrLen += rowStrLen + 1
            else:
                break

        modsJson = json.dumps(tmpMods)
        super(ModsStatisticLogger, self)._log(self.ACTION, mods_statistic_json=modsJson, total_mods=len(mods))
        ModsStatisticLogger.__alreadyLogged = True
