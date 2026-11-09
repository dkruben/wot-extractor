# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/st_patrick_banner.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/st_patrick_banner.py
from __future__ import absolute_import
from battle_royale.gui.impl.lobby.views.event_banner import BattleRoyaleEventBanner
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.lobby.user_missions.hangar_widget.event_banners.event_banners_container import EventBannersContainer
from helpers import dependency
from skeletons.gui.game_control import IBattleRoyaleController

@dependency.replace_none_kwargs(battleRoyaleController=IBattleRoyaleController)
def isStPatrickEntryPointAvailable(battleRoyaleController=None):
    return battleRoyaleController.isActive() and battleRoyaleController.isStPatrick()


class StPatrickEventBanner(BattleRoyaleEventBanner):
    NAME = 'StPatrickEntryPoint'

    @property
    def borderColor(self):
        return '#32FF7F'

    @property
    def introDescription(self):
        return backport.text(R.strings.hangar_event_banners.event.StPatrickEntryPoint.intro.description())

    @property
    def inProgressDescription(self):
        return backport.text(R.strings.hangar_event_banners.event.StPatrickEntryPoint.inProgress.description())

    def _onUpdate(self, *_):
        if isStPatrickEntryPointAvailable():
            EventBannersContainer().onBannerUpdate(self)
        else:
            self.__eventsService.updateEntries()
