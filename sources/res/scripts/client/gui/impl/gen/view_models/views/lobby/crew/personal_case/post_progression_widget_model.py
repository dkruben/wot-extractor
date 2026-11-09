# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/personal_case/post_progression_widget_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/personal_case/post_progression_widget_model.py
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.crew.components.component_base_model import ComponentBaseModel

class PostProgressionWidgetModel(ComponentBaseModel):
    __slots__ = ('onWidgetClick', )

    def __init__(self, properties=5, commands=1):
        super(PostProgressionWidgetModel, self).__init__(properties=properties, commands=commands)

    def getIcon(self):
        return self._getResource(1)

    def setIcon(self, value):
        self._setResource(1, value)

    def getProgressCurrent(self):
        return self._getNumber(2)

    def setProgressCurrent(self, value):
        self._setNumber(2, value)

    def getProgressMax(self):
        return self._getNumber(3)

    def setProgressMax(self, value):
        self._setNumber(3, value)

    def getHasWarning(self):
        return self._getBool(4)

    def setHasWarning(self, value):
        self._setBool(4, value)

    def _initialize(self):
        super(PostProgressionWidgetModel, self)._initialize()
        self._addResourceProperty('icon', R.invalid())
        self._addNumberProperty('progressCurrent', 0)
        self._addNumberProperty('progressMax', 0)
        self._addBoolProperty('hasWarning', False)
        self.onWidgetClick = self._addCommand('onWidgetClick')
