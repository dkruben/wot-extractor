# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/nation_change/NationChangeSettings.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/nation_change/NationChangeSettings.py
from __future__ import absolute_import
from future.utils import viewvalues
from typing import List, Dict, Iterable
from items import _xml
from realm_utils import ResMgr

class NationGroup(object):
    __slots__ = ('ID', 'tankList')

    def __init__(self, ID):
        self.ID = ID
        self.tankList = []


class NationChangeSettings(object):

    def __init__(self, xmlPath):
        self.__groupById = self.__readSettings(xmlPath)

    def getGroupById(self, groupId):
        return self.__groupById.get(groupId)

    def findVehicleGroup(self, vehicleTypeName):
        for group in viewvalues(self.__groupById):
            if vehicleTypeName in group.tankList:
                return group

        return

    def iterGroups(self):
        return viewvalues(self.__groupById)

    @staticmethod
    def __readSettings(xmlPath):
        configXml = ResMgr.openSection(xmlPath)
        if configXml is None:
            _xml.raiseWrongXml(None, xmlPath, 'can not open or read')
        xmlCtx = (None, xmlPath)
        unique = set()
        resDict = {}
        for id_, childSection in enumerate(_xml.getChildren(xmlCtx, configXml, 'nation_groups')):
            _, changeableVehicles = childSection
            for vehicle in changeableVehicles.values():
                vehicleType = vehicle.asString
                if vehicleType in unique:
                    ctx = (
                     xmlCtx, 'group')
                    _xml.raiseWrongXml(ctx, '', '%s is not unique' % (vehicleType,))
                    continue
                unique.add(vehicleType)
                nationGroup = resDict.setdefault(id_, NationGroup(id_))
                nationGroup.tankList.append(vehicleType)

        ResMgr.purge(xmlPath, True)
        return resDict
