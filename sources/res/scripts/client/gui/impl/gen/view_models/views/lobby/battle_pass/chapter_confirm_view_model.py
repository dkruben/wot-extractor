# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/chapter_confirm_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/chapter_confirm_view_model.py
from frameworks.wulf import ViewModel

class ChapterConfirmViewModel(ViewModel):
    __slots__ = ('onAccept', 'onCancel')

    def __init__(self, properties=3, commands=2):
        super(ChapterConfirmViewModel, self).__init__(properties=properties, commands=commands)

    def getPrevChapter(self):
        return self._getNumber(0)

    def setPrevChapter(self, value):
        self._setNumber(0, value)

    def getNextChapter(self):
        return self._getNumber(1)

    def setNextChapter(self, value):
        self._setNumber(1, value)

    def getIsSwitchFromPostProgressionToExtraChapter(self):
        return self._getBool(2)

    def setIsSwitchFromPostProgressionToExtraChapter(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(ChapterConfirmViewModel, self)._initialize()
        self._addNumberProperty('prevChapter', 0)
        self._addNumberProperty('nextChapter', 0)
        self._addBoolProperty('isSwitchFromPostProgressionToExtraChapter', False)
        self.onAccept = self._addCommand('onAccept')
        self.onCancel = self._addCommand('onCancel')
