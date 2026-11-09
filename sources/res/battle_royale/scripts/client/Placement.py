# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/Placement.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/Placement.py
from __future__ import absolute_import
import BigWorld
from constants import AirdropType
from debug_utils import LOG_DEBUG_DEV, LOG_ERROR
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from battle_royale.gui.shared.events import AirDropEvent

class IPlacementHandler(object):

    def onCreated(self, placement):
        pass

    def onDestroyed(self, placement):
        pass


class _AirDropCmpHandler(IPlacementHandler):
    __guiSessionProvider = dependency.descriptor(IBattleSessionProvider)
    __CMP_NAME = 'airDropComponent'

    def _getAirdropCmp(self):
        cmpSystem = self.__guiSessionProvider.arenaVisitor.getComponentSystem()
        if cmpSystem:
            return getattr(cmpSystem, self.__CMP_NAME)
        else:
            LOG_ERROR(("Couldn't find {}!").format(self.__CMP_NAME))
            return


class _AirdropLootHandler(_AirDropCmpHandler):

    def onCreated(self, placement):
        event = AirDropEvent(AirDropEvent.AIR_DROP_SPAWNED, ctx={'id': (placement.id), 'position': (placement.position)})
        g_eventBus.handleEvent(event, scope=EVENT_BUS_SCOPE.BATTLE)
        acmp = self._getAirdropCmp()
        if acmp:
            acmp.scheduleLoot(placement.id, placement.position, placement.dropTime)

    def onDestroyed(self, placement):
        event = AirDropEvent(AirDropEvent.AIR_DROP_LANDED, ctx={'id': (placement.id)})
        g_eventBus.handleEvent(event, scope=EVENT_BUS_SCOPE.BATTLE)


class _AirdropBotHandler(_AirDropCmpHandler):

    def onCreated(self, placement):
        acmp = self._getAirdropCmp()
        if acmp:
            acmp.scheduleBot(placement.id, placement.position, placement.teamID, placement.yawAxis, placement.dropTime, placement.typeID)


_TYPE_TO_PLACEMENT = {(AirdropType.LOOT): _AirdropLootHandler, 
   (AirdropType.BOT): _AirdropBotHandler, 
   (AirdropType.BOT_CLING): _AirdropBotHandler}

class Placement(BigWorld.Entity):

    def __init__(self):
        self.__handler = None
        return

    def onEnterWorld(self, *args):
        self.__handler = _TYPE_TO_PLACEMENT[self.typeID]()
        LOG_DEBUG_DEV(('[Placement] type={} onEnterWorld').format(self.typeID), BigWorld.time())
        self.__handler.onCreated(self)

    def onLeaveWorld(self):
        LOG_DEBUG_DEV(('[Placement] type={} onLeaveWorld').format(self.typeID), BigWorld.time())
        self.__handler.onDestroyed(self)
        self.__handler = None
        return
