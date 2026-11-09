# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/commendations_common/CommendationHelpers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/commendations_common/CommendationHelpers.py
from __future__ import absolute_import
import typing
from collections import namedtuple
import BigWorld
from constants import CommendationsState, IS_CLIENT, ARENA_PERIOD
AVATAR_COMPONENT_NAME = 'commendations'
ARENA_COMPONENT_NAME = 'ArenaCommendationsMasterComponent'
ARENA_CONTROLLER_NAME = 'commendationsController'
TEAM_INFO_LIVETAGS_COMPONENT = 'liveTagsInfoComponent'

class CommendationsSource(object):
    EARS = 'ears'
    TAB_SCREEN = 'tab'
    CALLOUT = 'callout'


def canCommendNow(period):
    return period in (ARENA_PERIOD.PREBATTLE, ARENA_PERIOD.BATTLE)


CommendationStatistics = namedtuple('CommendationStatistics', 'received, sent')
if typing.TYPE_CHECKING:
    CommendationsStatisticsType = typing.Union[(CommendationStatistics, typing.Tuple)]

def getCommendationState(vehicleID):
    cmpt = getAvatarComponent(BigWorld.player())
    return cmpt.getMessageStateForVehID(vehicleID)


def getAvatarComponent(entity):
    if not entity:
        return
    else:
        return entity.dynamicComponents.get(AVATAR_COMPONENT_NAME, None)


def getArenaComponent(entity):
    if not entity:
        return
    else:
        return entity.components.get(ARENA_COMPONENT_NAME, None)


def getArenaController(entity):
    if not entity:
        return
    else:
        return entity.dynamicComponents.get(ARENA_CONTROLLER_NAME, None)


def getTeamInfoLiveTagsComponent(entity):
    if not entity:
        return
    else:
        return entity.dynamicComponents.get(TEAM_INFO_LIVETAGS_COMPONENT, None)


CommendationStateType = typing.Union[(CommendationsState, int)]
