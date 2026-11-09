# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/lobby/header/helpers/controls_helpers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/scaleform/daapi/view/lobby/header/helpers/controls_helpers.py
from __future__ import absolute_import
from gui.impl.gen import R
from gui.Scaleform.daapi.view.lobby.header.helpers.controls_helpers import DefaultLobbyHeaderHelper
from halloween.gui.impl.lobby.page.hw_lobby_header import HWLobbyHeader
from halloween.gui.scaleform.daapi.view.lobby.header.helpers.fight_btn_tooltips import getHalloweenFightButtonTooltipData

class HalloweenLobbyHeaderHelper(DefaultLobbyHeaderHelper):
    __slots__ = ()

    @classmethod
    def getHeaderType(cls):
        return HWLobbyHeader

    @classmethod
    def _getDisabledFightTooltipData(cls, prbValidation, isInSquad):
        return (getHalloweenFightButtonTooltipData(prbValidation, isInSquad), False)

    @classmethod
    def _getOutSquadTooltipData(cls, _):
        squad = R.strings.halloween_platoon.headerButton.tooltips.squad
        return (squad.header(), squad.body(), {})
