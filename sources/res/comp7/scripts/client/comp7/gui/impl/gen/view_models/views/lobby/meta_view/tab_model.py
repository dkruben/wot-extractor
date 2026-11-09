# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/meta_view/tab_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/meta_view/tab_model.py
from comp7.gui.impl.gen.view_models.views.lobby.enums import MetaRootViews
from frameworks.wulf import ViewModel

class TabModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(TabModel, self).__init__(properties=properties, commands=commands)

    def getId(self):
        return MetaRootViews(self._getNumber(0))

    def setId(self, value):
        self._setNumber(0, value.value)

    def getHasNotification(self):
        return self._getBool(1)

    def setHasNotification(self, value):
        self._setBool(1, value)

    def _initialize(self):
        super(TabModel, self)._initialize()
        self._addNumberProperty('id')
        self._addBoolProperty('hasNotification', False)
