# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/mode_selector/items/spec_mode_selector_item.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/mode_selector/items/spec_mode_selector_item.py
import operator
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.lobby.mode_selector.items.base_item import ModeSelectorLegacyItem
from gui.prb_control.entities.battle_session.legacy.requester import AutoInvitesRequester
from helpers import dependency
from shared_utils import first
from skeletons.gui.impl import IGuiLoader

class SpecModeSelectorItem(ModeSelectorLegacyItem):
    __slots__ = ('__requester', )
    __guiLoader = dependency.descriptor(IGuiLoader)

    def handleClick(self):
        from gui.impl.lobby.mode_selector.states import BattleSessionState
        BattleSessionState.goTo()

    def _getIsDisabled(self):
        return False

    def _onInitializing(self):
        super(SpecModeSelectorItem, self)._onInitializing()
        self.__requester = AutoInvitesRequester()
        self.__requester.start(self.__onListReceived)
        self.__requester.request()

    def _onDisposing(self):
        self.__requester.stop()
        super(SpecModeSelectorItem, self)._onDisposing()

    def __onListReceived(self, sessions):
        item = first(sorted(sessions, key=operator.attrgetter('startTime')))
        if item:
            self.viewModel.setStatusActive(backport.text(R.strings.mode_selector.mode.specBattlesList.call.c_2(), date=backport.getShortDateFormat(item.startTime), time=backport.getShortTimeFormat(item.startTime)))
        else:
            self.viewModel.setStatusActive(backport.text(R.strings.mode_selector.mode.specBattlesList.call.c_1()))
