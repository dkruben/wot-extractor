# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/helpers/fixed_dict.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/fixed_dict.py
from __future__ import absolute_import
import typing
from collections import namedtuple
RoleEquipmentState = namedtuple('RoleEquipmentState', ('level', 'progress'))
StatusWithTimeInterval = namedtuple('StatusWithTimeInterval', ('statusID', 'startTime',
                                                               'endTime'))
TimeInterval = namedtuple('TimeInterval', ('startTime', 'endTime'))
StateWithTimeInterval = namedtuple('TimeInterval', ('stateID', 'timeInterval', 'isSourceVehicle'))
VisualScriptEquipmentState = namedtuple('VisualScriptEquipmentState', ('quantity',
                                                                       'endTime',
                                                                       'totalTime',
                                                                       'prevStage',
                                                                       'stage', 'locked'))
VisualScriptEquipmentPublicState = namedtuple('VisualScriptEquipmentPublicState', ('stage', ))
if typing.TYPE_CHECKING:
    from enum import Enum

def getRoleEquipmentState(fixedDict):
    state = RoleEquipmentState(level=fixedDict['level'], progress=fixedDict['progress'])
    return state


def getStatusWithTimeInterval(fixedDict, statusEnum=None):
    status = StatusWithTimeInterval(statusID=statusEnum(fixedDict['statusID']) if statusEnum is not None else fixedDict['statusID'], startTime=fixedDict['startTime'], endTime=fixedDict['endTime'])
    return status


def getTimeInterval(fixedDict):
    interval = TimeInterval(startTime=fixedDict['startTime'], endTime=fixedDict['endTime'])
    return interval


def getStateWithTimeInterval(fixedDict):
    state = StateWithTimeInterval(stateID=fixedDict['stateID'], timeInterval=getTimeInterval(fixedDict['timeInterval']), isSourceVehicle=fixedDict['isSourceVehicle'])
    return state


def getVisualScriptEquipmentState(fixedDict):
    state = VisualScriptEquipmentState(quantity=fixedDict['quantity'], endTime=fixedDict['endTime'], totalTime=fixedDict['totalTime'], prevStage=fixedDict['prevStage'], stage=fixedDict['stage'], locked=fixedDict['locked'])
    return state


def getVisualScriptEquipmentPublicState(fixedDict):
    state = VisualScriptEquipmentPublicState(stage=fixedDict['stage'])
    return state
