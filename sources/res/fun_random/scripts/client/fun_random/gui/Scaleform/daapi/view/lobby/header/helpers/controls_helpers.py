# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/Scaleform/daapi/view/lobby/header/helpers/controls_helpers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/Scaleform/daapi/view/lobby/header/helpers/controls_helpers.py
from __future__ import absolute_import
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin
from fun_random.gui.Scaleform.daapi.view.lobby.header.helpers.fight_btn_tooltips import getFunRandomFightBtnTooltipData
from gui.impl.gen import R
from gui.Scaleform.daapi.view.lobby.header.helpers.controls_helpers import DefaultLobbyHeaderHelper

class FunRandomLobbyHeaderHelper(DefaultLobbyHeaderHelper, FunAssetPacksMixin):
    __slots__ = ()

    @classmethod
    def _getDisabledFightTooltipData(cls, prbValidation, isInSquad):
        return (getFunRandomFightBtnTooltipData(prbValidation, isInSquad), False)

    @classmethod
    def _getOutSquadTooltipData(cls, _):
        squad = R.strings.fun_random.headerButtons.tooltips.funRandomSquad
        return (squad.header(), squad.body(), {'modeName': (cls.getModeUserName())})
