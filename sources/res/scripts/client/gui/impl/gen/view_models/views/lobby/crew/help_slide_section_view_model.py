# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/help_slide_section_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/help_slide_section_view_model.py
from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen import R

class SlideSectionSize(Enum):
    SMALL = 'small'
    BIG = 'big'


class HelpSlideSectionViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(HelpSlideSectionViewModel, self).__init__(properties=properties, commands=commands)

    def getImage(self):
        return self._getResource(0)

    def setImage(self, value):
        self._setResource(0, value)

    def getDescription(self):
        return self._getResource(1)

    def setDescription(self, value):
        self._setResource(1, value)

    def getSize(self):
        return SlideSectionSize(self._getString(2))

    def setSize(self, value):
        self._setString(2, value.value)

    def _initialize(self):
        super(HelpSlideSectionViewModel, self)._initialize()
        self._addResourceProperty('image', R.invalid())
        self._addResourceProperty('description', R.invalid())
        self._addStringProperty('size')
