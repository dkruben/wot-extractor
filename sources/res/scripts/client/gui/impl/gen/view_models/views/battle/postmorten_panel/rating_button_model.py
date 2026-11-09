# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/battle/postmorten_panel/rating_button_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle/postmorten_panel/rating_button_model.py
from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen import R

class RateButtonEnum(Enum):
    WORSE = 'worse'
    USUAL = 'usual'
    BETTER = 'better'
    UNSET = 'unset'


class RatingButtonModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(RatingButtonModel, self).__init__(properties=properties, commands=commands)

    def getButtonVariant(self):
        return RateButtonEnum(self._getString(0))

    def setButtonVariant(self, value):
        self._setString(0, value.value)

    def getFeedbackString(self):
        return self._getResource(1)

    def setFeedbackString(self, value):
        self._setResource(1, value)

    def _initialize(self):
        super(RatingButtonModel, self)._initialize()
        self._addStringProperty('buttonVariant')
        self._addResourceProperty('feedbackString', R.invalid())
