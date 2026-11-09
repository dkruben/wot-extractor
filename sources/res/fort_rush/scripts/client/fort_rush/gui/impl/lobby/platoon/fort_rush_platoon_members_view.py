# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/platoon/fort_rush_platoon_members_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/impl/lobby/platoon/fort_rush_platoon_members_view.py
from __future__ import absolute_import
from enum import Enum
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.lobby.platoon.view.platoon_members_view import SquadMembersView
from helpers import i18n

class _PrebattleTypes(Enum):
    FORT_RUSH = 'fort_rush'


class FortRushPlatoonMembersView(SquadMembersView):
    _prebattleType = _PrebattleTypes.FORT_RUSH

    def _onLoading(self):
        super(FortRushPlatoonMembersView, self)._onLoading()
        self.viewModel.setShouldShowFindPlayersButton(False)

    def _onFindPlayers(self):
        pass

    def _getTitle(self):
        title = ('').join((
         i18n.makeString(backport.text(R.strings.platoon.squad())),
         i18n.makeString(backport.text(R.strings.platoon.members.header.fort_rush()))))
        return title

    def _getWindowInfoTooltipHeaderAndBody(self):
        tooltipHeader = backport.text(R.strings.platoon.fort_rush.members.header.tooltip.header())
        tooltipBody = backport.text(R.strings.platoon.fort_rush.members.header.tooltip.body())
        return (tooltipHeader, tooltipBody)
