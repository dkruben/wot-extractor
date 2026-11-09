# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/battle/shared/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/battle/shared/__init__.py
from __future__ import absolute_import
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.battle import shared

def getContextMenuHandlers():
    return shared.getContextMenuHandlers()


def getViewSettings():
    from battle_royale.gui.Scaleform.daapi.view.battle.shared.br_ingame_menu import BRIngameMenu
    settingsList = []
    for viewSetting in shared.getViewSettings():
        if viewSetting.alias == VIEW_ALIAS.INGAME_MENU:
            viewSetting = viewSetting._replace(clazz=BRIngameMenu)
        settingsList.append(viewSetting)

    return settingsList


def getBusinessHandlers():
    return shared.getBusinessHandlers()
