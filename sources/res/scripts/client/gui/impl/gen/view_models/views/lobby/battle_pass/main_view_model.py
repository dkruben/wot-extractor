# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/main_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/main_view_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.common.router_model import RouterModel

class MainViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(MainViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def router(self):
        return self._getViewModel(0)

    @staticmethod
    def getRouterType():
        return RouterModel

    def _initialize(self):
        super(MainViewModel, self)._initialize()
        self._addViewModelProperty('router', RouterModel())
