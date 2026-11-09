# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/lobby/header/helpers/fight_btn_tooltips.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/lobby/header/helpers/fight_btn_tooltips.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.lobby.header.helpers.fight_btn_tooltips import getRandomTooltipData, getSquadFightBtnTooltipData
from gui.impl import backport
from gui.impl.gen import R
from gui.prb_control.settings import PRE_QUEUE_RESTRICTION, UNIT_RESTRICTION
from gui.shared.utils.functions import makeTooltip

def getLSFightButtonTooltipData(result, isInSquad):
    state = result.restriction
    if state == PRE_QUEUE_RESTRICTION.MODE_NOT_AVAILABLE:
        header = backport.text(R.strings.last_stand_tooltips.hangar.startBtn.offline.header())
        body = backport.text(R.strings.last_stand_tooltips.hangar.startBtn.offline.body())
        return makeTooltip(header, body)
    if state == PRE_QUEUE_RESTRICTION.VEHICLE_WILL_BE_UNLOCKED:
        header = backport.text(R.strings.last_stand_tooltips.hangar.startBtn.lock.header())
        body = backport.text(R.strings.last_stand_tooltips.hangar.startBtn.lock.body())
        return makeTooltip(header, body)
    if isInSquad:
        return getLSSquadFightBtnTooltipData(result)
    return getRandomTooltipData(result, isInSquad)


def getLSSquadFightBtnTooltipData(result):
    state = result.restriction
    if state == UNIT_RESTRICTION.MODE_NOT_AVAILABLE:
        header = backport.text(R.strings.last_stand_tooltips.hangar.startBtn.offline.header())
        body = backport.text(R.strings.last_stand_tooltips.hangar.startBtn.offline.body())
    elif state == UNIT_RESTRICTION.IS_IN_ARENA:
        header = backport.text(R.strings.last_stand_tooltips.hangar.startBtn.squadInBattle.header())
        body = backport.text(R.strings.last_stand_tooltips.hangar.startBtn.squadInBattle.body())
    elif state == UNIT_RESTRICTION.VEHICLE_NOT_VALID:
        header = backport.text(R.strings.last_stand_tooltips.hangar.startBtn.lock.header())
        body = backport.text(R.strings.last_stand_tooltips.hangar.startBtn.lock.body())
    elif state == UNIT_RESTRICTION.UNIT_WRONG_DATA:
        header = backport.text(R.strings.last_stand_tooltips.hangar.startBtn.squadNotAvailableLevel.header())
        body = backport.text(R.strings.last_stand_tooltips.hangar.startBtn.squadNotAvailableLevel.body())
    else:
        return getSquadFightBtnTooltipData(result)
    return makeTooltip(header, body)
