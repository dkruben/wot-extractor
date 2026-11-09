# wot-extractor: codigo DESCOMPILADO de sources/res/server_side_replay/scripts/client/server_side_replay/gui/Scaleform/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: server_side_replay/scripts/client/server_side_replay/gui/Scaleform/__init__.py
from __future__ import absolute_import
from server_side_replay.gui.shared.event_dispatcher import showReplays
from gui.shared.system_factory import registerMenuItems
from helpers import dependency
from skeletons.gui.shared import IItemsCache

@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def isSsrPlayEnabled(itemsCache=None):
    return itemsCache.items.stats.isSsrPlayEnabled


def registerMainMenuEntries():
    from gui.impl.gen.view_models.views.lobby.hangar.main_menu_model import MainMenuModel
    from gui.impl.lobby.hangar.presenters.utils import MenuItemEntry
    menuItems = {(MainMenuModel.REPLAYS): (MenuItemEntry(showReplays, isSsrPlayEnabled, isSsrPlayEnabled))}
    registerMenuItems('hangar', menuItems)
