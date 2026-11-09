# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/server_events/bonuses.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/server_events/bonuses.py
from __future__ import absolute_import
from gui.server_events.bonuses import TokensBonus
from last_stand_common.last_stand_constants import BoostersSettings, ProgressPointsSettings

def boosterTokenChecker(tokenID):
    return tokenID.startswith(BoostersSettings.TOKEN_PREFIX)


class BoosterTokenBonus(TokensBonus):

    def __init__(self, name, value, isCompensation=False, ctx=None):
        super(TokensBonus, self).__init__(BoostersSettings.BONUS_NAME, value, isCompensation, ctx)

    def isShowInGUI(self):
        return True


def progressPointTokenChecker(tokenID):
    return tokenID == ProgressPointsSettings.TOKEN


class ProgressPointTokenBonus(TokensBonus):

    def __init__(self, name, value, isCompensation=False, ctx=None):
        super(TokensBonus, self).__init__(ProgressPointsSettings.BONUS_NAME, value.get(ProgressPointsSettings.TOKEN, {}), isCompensation, ctx)

    def isShowInGUI(self):
        return True
