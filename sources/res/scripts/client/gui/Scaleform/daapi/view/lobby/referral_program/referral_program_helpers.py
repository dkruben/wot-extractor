# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/referral_program/referral_program_helpers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/referral_program/referral_program_helpers.py
from __future__ import absolute_import
from gui import GUI_SETTINGS
from helpers import dependency
from skeletons.gui.shared import IItemsCache
RECRUITER_SPA_ID_ATTR = '/wot/game/ref/recruiterSpaId'

def _getUrl(urlName=None):
    if urlName is None:
        return getReferralProgramURL()
    else:
        return getReferralProgramURL() + GUI_SETTINGS.referralProgram.get(urlName)


def getReferralProgramURL():
    return GUI_SETTINGS.referralProgram.get('baseUrl')


def getObtainVehicleURL():
    return _getUrl('getVehicle')


@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def isCurrentUserRecruit(itemsCache=None):
    return bool(itemsCache.items.stats.SPA.get(RECRUITER_SPA_ID_ATTR, False))
