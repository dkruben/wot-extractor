# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/shared/contexts.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/shared/contexts.py
from __future__ import absolute_import
from gui.shared.tooltips.contexts import CarouselContext

class EventVehicleContext(CarouselContext):

    def __init__(self, fieldsToExclude=None):
        super(EventVehicleContext, self).__init__(fieldsToExclude)
        self.__isShort = False

    def buildItem(self, intCD, isShort=False, *args):
        self.__isShort = isShort
        return self.itemsCache.items.getItemByCD(int(intCD))

    def getParams(self):
        return {'isShort': (self.__isShort)}
