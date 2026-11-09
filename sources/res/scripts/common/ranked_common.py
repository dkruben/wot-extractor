# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/ranked_common.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/ranked_common.py
from __future__ import absolute_import
import season_common

def getShieldsConfig(rankedConfig, now):
    result = {}
    res, seasonInfo = season_common.getSeason(rankedConfig, now)
    if not res:
        return result
    _, _, seasonID, cycleID = seasonInfo
    season = rankedConfig['seasons'].get(seasonID)
    if season:
        cycle = season['cycles'].get(cycleID, {})
        result.update(cycle.get('shields', rankedConfig['shields']))
    return result


class SwitchState(object):
    ENABLED = 'enabled'
    DISABLED = 'disabled'
    HIDDEN = 'hidden'
    ALL = ('enabled', 'disabled', 'hidden')
