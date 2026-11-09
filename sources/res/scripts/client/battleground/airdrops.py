# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/battleground/airdrops.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/battleground/airdrops.py
from __future__ import absolute_import
from constants import AirdropType
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from arena_component_system.client_arena_component_system import ClientArenaComponent
from battleground.bot_drop_object import BotAirdrop
from battleground.loot_drop_object import PlaneLootAirdrop

class Airdrops(object):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def scheduleLoot(self, dropID, position, serverTime):
        planeObj = PlaneLootAirdrop(dropID, position, serverTime)
        planeObj.start()

    def scheduleBot(self, dropID, position, teamID, yawAxis, serverTime, airdropType=AirdropType.BOT):
        botObj = BotAirdrop(dropID, position, teamID, yawAxis, serverTime, airdropType)
        botObj.start()


class AirdropsComponent(ClientArenaComponent, Airdrops):

    def __init__(self, componentSystem):
        Airdrops.__init__(self)
        ClientArenaComponent.__init__(self, componentSystem)
