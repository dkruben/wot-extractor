# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/tooltips/directive_conversion_tooltip_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/tooltips/directive_conversion_tooltip_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.crew.tooltips.directive_conversion_directive_model import DirectiveConversionDirectiveModel

class DirectiveConversionTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(DirectiveConversionTooltipModel, self).__init__(properties=properties, commands=commands)

    @property
    def oldDirective(self):
        return self._getViewModel(0)

    @staticmethod
    def getOldDirectiveType():
        return DirectiveConversionDirectiveModel

    @property
    def newDirective(self):
        return self._getViewModel(1)

    @staticmethod
    def getNewDirectiveType():
        return DirectiveConversionDirectiveModel

    def getAmount(self):
        return self._getNumber(2)

    def setAmount(self, value):
        self._setNumber(2, value)

    def _initialize(self):
        super(DirectiveConversionTooltipModel, self)._initialize()
        self._addViewModelProperty('oldDirective', DirectiveConversionDirectiveModel())
        self._addViewModelProperty('newDirective', DirectiveConversionDirectiveModel())
        self._addNumberProperty('amount', 0)
