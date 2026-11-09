# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/shared/event_dispatcher.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/shared/event_dispatcher.py
from __future__ import absolute_import

def showComp7LightNoVehiclesScreen():
    from comp7_light.gui.impl.lobby.hangar.states import Comp7LightNoVehiclesState
    Comp7LightNoVehiclesState.goTo()


def showComp7LightIntroScreen():
    from comp7_light.gui.impl.lobby.hangar.states import Comp7LightIntroState
    Comp7LightIntroState.goTo()


def showComp7LightProgressionView():
    from comp7_light.gui.impl.lobby.hangar.states import Comp7LightProgressionState
    Comp7LightProgressionState.goTo()


def showComp7LightPrimeTimeWindow():
    from comp7_light.gui.impl.lobby.hangar.states import Comp7LightPrimeTimeState
    Comp7LightPrimeTimeState.goTo()


def showComp7LightInfoPage():
    from comp7_light.gui.comp7_light_constants import SELECTOR_BATTLE_TYPES
    from frameworks.wulf import WindowLayer
    from gui import GUI_SETTINGS
    from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
    from gui.impl.lobby.mode_selector.items.base_item import getInfoPageKey
    from gui.shared.event_dispatcher import showBrowserOverlayView
    url = GUI_SETTINGS.lookup(getInfoPageKey(SELECTOR_BATTLE_TYPES.COMP7_LIGHT))
    showBrowserOverlayView(url, VIEW_ALIAS.WEB_VIEW_TRANSPARENT, hiddenLayers=(
     WindowLayer.MARKER, WindowLayer.VIEW, WindowLayer.WINDOW))


def showBattleQuestAwardsWindow(stage):
    from comp7_light.gui.impl.lobby.battle_quest_awards_view import BattleQuestAwardsViewWindow
    window = BattleQuestAwardsViewWindow(stage)
    window.load()
