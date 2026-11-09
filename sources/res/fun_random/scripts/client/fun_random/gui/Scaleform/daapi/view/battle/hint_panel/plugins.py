# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/Scaleform/daapi/view/battle/hint_panel/plugins.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/Scaleform/daapi/view/battle/hint_panel/plugins.py
from __future__ import absolute_import
from account_helpers import AccountSettings
from account_helpers.AccountSettings import FUN_RANDOM_HINT_SECTION, HINTS_LEFT
from fun_random.gui.Scaleform.daapi.view.battle.hint_panel.hint_panel_plugin import HelpHintContext
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasBattleSubMode
from gui.Scaleform.daapi.view.battle.shared.hint_panel.hint_panel_plugin import HintPriority
from gui.Scaleform.daapi.view.battle.shared.hint_panel.plugins import PreBattleHintPlugin, HelpPlugin

def updatePlugins(plugins):
    if FunRandomPreBattleHintPlugin.isSuitable():
        plugins['prebattleHints'] = FunRandomPreBattleHintPlugin
    else:
        plugins.pop('prebattleHints', None)
    if FunRandomHelpPlugin.isSuitable():
        plugins['funRandomHelpHint'] = FunRandomHelpPlugin
    return plugins


class FunRandomPreBattleHintPlugin(PreBattleHintPlugin, FunSubModesWatcher):

    @classmethod
    @hasBattleSubMode(defReturn=False)
    def isSuitable(cls):
        settingsKey = cls.getBattleSubMode().getSettings().client.settingsKey
        funRandomSettings = AccountSettings.getSettings(FUN_RANDOM_HINT_SECTION)
        return settingsKey in funRandomSettings and funRandomSettings[settingsKey][HINTS_LEFT] <= 0


class FunRandomHelpPlugin(HelpPlugin, FunSubModesWatcher):

    def __init__(self, parentObj):
        battleSubMode = self.getBattleSubMode()
        super(FunRandomHelpPlugin, self).__init__(FUN_RANDOM_HINT_SECTION, battleSubMode.getSettings().client.settingsKey, battleSubMode.getLocalsResRoot().detailsHelpHint, HintPriority.HELP, HelpHintContext.FUN_RANDOM, parentObj)

    @classmethod
    @hasBattleSubMode(defReturn=False)
    def isSuitable(cls):
        settingsKey = cls.getBattleSubMode().getSettings().client.settingsKey
        funRandomSettings = AccountSettings.getSettings(FUN_RANDOM_HINT_SECTION)
        return settingsKey not in funRandomSettings or funRandomSettings[settingsKey][HINTS_LEFT] > 0
