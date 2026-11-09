# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/lobby/header/helpers/controls_helpers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/lobby/header/helpers/controls_helpers.py
from __future__ import absolute_import
from gui.impl.gen import R
from gui.Scaleform.daapi.view.lobby.header.helpers.controls_helpers import DefaultLobbyHeaderHelper
from gui.Scaleform.daapi.view.lobby.header.helpers.fight_btn_tooltips import getRoyaleFightBtnTooltipData
from battle_royale.gui.Scaleform.daapi.view.lobby.footer.battle_royale_lobby_footer import BattleRoyaleLobbyFooter

class BattleRoyaleLobbyHeaderHelper(DefaultLobbyHeaderHelper):
    _IN_SQUAD_TOOLTIP_KEY = 'battleRoyaleSquad'
    _OUT_SQUAD_TOOLTIP_KEY = 'battleRoyaleSquad'

    @classmethod
    def _getDisabledFightTooltipData(cls, prbValidation, isInSquad):
        return (getRoyaleFightBtnTooltipData(prbValidation), False)

    @classmethod
    def getFooterType(cls):
        return BattleRoyaleLobbyFooter


class BRTournamentLobbyHeaderHelper(DefaultLobbyHeaderHelper):
    __slots__ = ()

    @classmethod
    def getFightControlTooltipData(cls, prbValidation, isInSquad, isFightBtnDisabled, isNavigationEnabled):
        return ('', False)

    @classmethod
    def getSquadControlTooltipData(cls, prbValidation, isInSquad):
        return (R.invalid(), R.invalid(), {})
