# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/buy_chapter_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/buy_chapter_model.py
from frameworks.wulf import ViewModel

class BuyChapterModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BuyChapterModel, self).__init__(properties=properties, commands=commands)

    def getChapterID(self):
        return self._getNumber(0)

    def setChapterID(self, value):
        self._setNumber(0, value)

    def getHasStarterPack(self):
        return self._getBool(1)

    def setHasStarterPack(self, value):
        self._setBool(1, value)

    def getIsExtra(self):
        return self._getBool(2)

    def setIsExtra(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(BuyChapterModel, self)._initialize()
        self._addNumberProperty('chapterID', 0)
        self._addBoolProperty('hasStarterPack', False)
        self._addBoolProperty('isExtra', False)
