# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/page/header/header_state_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/page/header/header_state_model.py
from enum import Enum
from frameworks.wulf import Map, ViewModel
from gui.impl.gen.view_models.views.lobby.common.router_model import RouterModel

class HeaderType(Enum):
    HANGAR = 'hangar'
    DEFAULT = 'default'


class HeaderStateModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(HeaderStateModel, self).__init__(properties=properties, commands=commands)

    @property
    def router(self):
        return self._getViewModel(0)

    @staticmethod
    def getRouterType():
        return RouterModel

    def getFeatures(self):
        return self._getMap(1)

    def setFeatures(self, value):
        self._setMap(1, value)

    @staticmethod
    def getFeaturesType():
        return (unicode, bool)

    def _initialize(self):
        super(HeaderStateModel, self)._initialize()
        self._addViewModelProperty('router', RouterModel())
        self._addMapProperty('features', Map(unicode, bool))
