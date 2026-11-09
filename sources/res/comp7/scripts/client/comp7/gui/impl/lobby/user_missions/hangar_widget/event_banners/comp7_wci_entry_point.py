# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/user_missions/hangar_widget/event_banners/comp7_wci_entry_point.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/lobby/user_missions/hangar_widget/event_banners/comp7_wci_entry_point.py
from __future__ import absolute_import
from comp7.gui.Scaleform.genConsts.COMP7_HANGAR_ALIASES import COMP7_HANGAR_ALIASES
from comp7.gui.comp7_constants import FUNCTIONAL_FLAG
from comp7.gui.impl.lobby.user_missions.hangar_widget.event_banners.comp7_tournament_event_banner import Comp7TournamentEventBanner
from comp7.gui.shared import event_dispatcher as comp7_events
from helpers.ingame_tournament_helper import IngameTournamentType
from skeletons.gui.game_control import IComp7Controller

class Comp7WCIEntryPoint(Comp7TournamentEventBanner):
    NAME = COMP7_HANGAR_ALIASES.COMP7_WCI_ENTRY_POINT
    _TOURNAMENT_TYPE = IngameTournamentType.WCI

    def onClick(self):
        comp7_events.showComp7WCIScreen()

    @classmethod
    def isTournamentEntryPointAvailable(cls, comp7Ctrl=None):
        return super(Comp7WCIEntryPoint, cls).isTournamentEntryPointAvailable() and cls.__isRandomPrbActive()

    @classmethod
    def __isRandomPrbActive(cls):
        if cls.prbEntity is not None:
            return bool(cls.prbEntity.getModeFlags() & FUNCTIONAL_FLAG.RANDOM)
        else:
            return False
