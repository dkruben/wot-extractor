# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/mode_selector/items/winback_mode_selector_item.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/mode_selector/items/winback_mode_selector_item.py
from account_helpers.AccountSettings import Winback, AccountSettings
from gui.Scaleform.daapi.view.lobby.header import battle_selector_items
from gui.impl.gen import R
from gui.impl.lobby.mode_selector.items.random_mode_selector_item import RandomModeSelectorItem
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel
from gui.prb_control.settings import PREBATTLE_ACTION_NAME
from gui.shared import g_eventBus
from gui.shared.events import ModeSelectorPopoverEvent
from gui.winback.winback_helpers import getWinbackSetting

class WinbackModeSelectorItem(RandomModeSelectorItem):

    @property
    def modeName(self):
        return PREBATTLE_ACTION_NAME.RANDOM

    def isSelected(self):
        return battle_selector_items.getItems().isSelected(PREBATTLE_ACTION_NAME.WINBACK)

    def getViewModel(self):
        return self.viewModel

    def _onInitializing(self):
        super(WinbackModeSelectorItem, self)._onInitializing()
        AccountSettings.onSettingsChanging += self.__onAccountSettingsChanging
        g_eventBus.addListener(ModeSelectorPopoverEvent.NAME, self.__onModeSelectorPopoverEvent)
        self.__fillCardModel()

    def _onDisposing(self):
        AccountSettings.onSettingsChanging -= self.__onAccountSettingsChanging
        g_eventBus.removeListener(ModeSelectorPopoverEvent.NAME, self.__onModeSelectorPopoverEvent)
        super(WinbackModeSelectorItem, self)._onDisposing()

    def _isInfoIconVisible(self):
        return False

    def __onAccountSettingsChanging(self, key, _):
        if key == Winback.WINBACK_SETTINGS:
            self.onCardChange()

    def __onModeSelectorPopoverEvent(self, event):
        self.viewModel.setIsSettingsActive(event.ctx['active'])

    @replaceNoneKwargsModel
    def __fillCardModel(self, model=None):
        isBattleSelectorSettingsBulletShown = getWinbackSetting(Winback.BATTLE_SELECTOR_SETTINGS_BULLET_SHOWN)
        model.setSettingsPopoverID(R.views.mono.winback.popovers.winback_leave_mode_popover_view())
        model.setWithSettingsNotification(not isBattleSelectorSettingsBulletShown)
        model.setIsSettingsActive(False)
