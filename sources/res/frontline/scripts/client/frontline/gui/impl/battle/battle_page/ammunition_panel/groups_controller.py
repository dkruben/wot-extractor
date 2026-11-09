# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/impl/battle/battle_page/ammunition_panel/groups_controller.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/impl/battle/battle_page/ammunition_panel/groups_controller.py
from __future__ import absolute_import
from constants import ARENA_GUI_TYPE
from frontline.constants.common import FRONTLINE_GROUPS
from gui.impl.battle.battle_page.ammunition_panel.groups_controller import RespawnAmmunitionGroupsController
from gui.impl.common.ammunition_panel.ammunition_groups_controller import RANDOM_GROUPS
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class FLRespawnAmmunitionGroupsController(RespawnAmmunitionGroupsController):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def _getGroups(self):
        arenaGuiType = self.__sessionProvider.arenaVisitor.getArenaGuiType()
        if arenaGuiType in (ARENA_GUI_TYPE.EPIC_BATTLE, ARENA_GUI_TYPE.EPIC_TRAINING):
            return FRONTLINE_GROUPS
        return RANDOM_GROUPS
