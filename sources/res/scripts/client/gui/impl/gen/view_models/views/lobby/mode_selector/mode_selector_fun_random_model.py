# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/mode_selector/mode_selector_fun_random_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/mode_selector/mode_selector_fun_random_model.py
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_fun_random_widget_model import ModeSelectorFunRandomWidgetModel
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_normal_card_model import ModeSelectorNormalCardModel

class ModeSelectorFunRandomModel(ModeSelectorNormalCardModel):
    __slots__ = ()

    def __init__(self, properties=23, commands=0):
        super(ModeSelectorFunRandomModel, self).__init__(properties=properties, commands=commands)

    @property
    def widget(self):
        return self._getViewModel(22)

    @staticmethod
    def getWidgetType():
        return ModeSelectorFunRandomWidgetModel

    def _initialize(self):
        super(ModeSelectorFunRandomModel, self)._initialize()
        self._addViewModelProperty('widget', ModeSelectorFunRandomWidgetModel())
