# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/user_missions/hangar_widget/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/user_missions/hangar_widget/__init__.py
from __future__ import absolute_import
import typing
if typing.TYPE_CHECKING:
    from helpers.dependency import DependencyManager
__all__ = ('getUserMissionsConfig', )

def getUserMissionsConfig(manager):
    from gui.impl.lobby.user_missions.hangar_widget.services import IBattlePassService, IEventsService, IMissionsService, IMissionsContainerService, IUserMissionWidgetService
    from gui.impl.lobby.user_missions.hangar_widget.services.battle_pass_service import BattlePassService
    from gui.impl.lobby.user_missions.hangar_widget.services.events_service import EventsService
    from gui.impl.lobby.user_missions.hangar_widget.services.missions_service import MissionsService
    from gui.impl.lobby.user_missions.hangar_widget.services.missions_container_service import MissionsContainerService
    from gui.impl.lobby.user_missions.hangar_widget.services.user_mission_widget_service import UserMissionWidgetService
    battlePassService = BattlePassService()
    manager.addInstance(IBattlePassService, battlePassService, finalizer='finalize')
    eventsService = EventsService()
    manager.addInstance(IEventsService, eventsService, finalizer='finalize')
    missionsService = MissionsService()
    manager.addInstance(IMissionsService, missionsService, finalizer='finalize')
    missionsContainerService = MissionsContainerService()
    manager.addInstance(IMissionsContainerService, missionsContainerService, finalizer='finalize')
    userMissionWidgetService = UserMissionWidgetService()
    manager.addInstance(IUserMissionWidgetService, userMissionWidgetService, finalizer='finalize')
