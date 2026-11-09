# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/vehicle_hub/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/vehicle_hub/__init__.py
from __future__ import absolute_import
from gui.impl.gen import R
from gui.impl.lobby.gf_notifications import GFNotificationTemplates
from gui.impl.lobby.veh_skill_tree.notifications.perk_available_notification import PerkAvailableNotification
from gui.impl.lobby.vehicle_hub.states import OverviewState, ModulesState, StatsState, ArmorState, VehSkillTreeState, VehSkillTreeInitialState, VehSkillTreePrestigeState, VehSkillTreeProgressionState
from gui.impl.lobby.vehicle_hub.vehicle_hub_main_view import VehicleHubCtx
from gui.shared.system_factory import registerGamefaceNotifications
__all__ = ('OverviewState', 'ModulesState', 'StatsState', 'ArmorState', 'VehSkillTreeState',
           'VehSkillTreeInitialState', 'VehSkillTreePrestigeState', 'VehSkillTreeProgressionState',
           'VehicleHubCtx')

def getStateMachineRegistrators():
    from gui.impl.lobby.vehicle_hub.states import registerStates, registerTransitions
    return (
     registerStates, registerTransitions)


def getContextMenuHandlers():
    return ()


def getViewSettings():
    return ()


def getBusinessHandlers():
    return ()


registerGamefaceNotifications({(GFNotificationTemplates.SKILL_TREE_PERK_AVAILABLE_NOTIFICATION): (
                                                                    R.views.mono.lobby.veh_skill_tree.notifications.perk_available(), PerkAvailableNotification)})
