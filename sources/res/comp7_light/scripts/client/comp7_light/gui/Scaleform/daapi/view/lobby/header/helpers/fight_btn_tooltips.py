# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/Scaleform/daapi/view/lobby/header/helpers/fight_btn_tooltips.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/Scaleform/daapi/view/lobby/header/helpers/fight_btn_tooltips.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.lobby.header.helpers.fight_btn_tooltips import getRandomTooltipData
from gui.impl import backport
from gui.impl.gen import R
from gui.periodic_battles.models import PrimeTimeStatus
from gui.shared.utils.functions import makeTooltip
from helpers import dependency, int2roman
from skeletons.gui.game_control import IComp7LightController

@dependency.replace_none_kwargs(comp7LightController=IComp7LightController)
def _getPrimeTimeStatus(comp7LightController=None):
    status, _, _ = comp7LightController.getPrimeTimeStatus()
    return status


@dependency.replace_none_kwargs(comp7LightController=IComp7LightController)
def getComp7LightFightBtnTooltipData(result, isInSquad, comp7LightController=None):
    resShortCut = R.strings.menu.headerButtons.fightBtn.tooltip
    if not comp7LightController.hasSuitableVehicles():
        romanLevels = list(map(int2roman, comp7LightController.getModeSettings().levels))
        delimiter = backport.text(resShortCut.comp7LightVehLevel.delimiter())
        vehicleLevelsStr = delimiter.join(romanLevels)
        header = backport.text(resShortCut.comp7LightVehLevel.header())
        body = backport.text(resShortCut.comp7LightVehLevel.body(), levels=vehicleLevelsStr)
    elif _getPrimeTimeStatus() != PrimeTimeStatus.AVAILABLE:
        header = backport.text(resShortCut.comp7LightDisabled.header())
        body = backport.text(resShortCut.comp7LightDisabled.body())
    else:
        return getRandomTooltipData(result, isInSquad)
    return makeTooltip(header, body)
