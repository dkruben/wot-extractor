# wot-extractor: codigo DESCOMPILADO de sources/res/resource_well/scripts/client/resource_well/gui/impl/gen/view_models/views/lobby/resources_tab_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: resource_well/scripts/client/resource_well/gui/impl/gen/view_models/views/lobby/resources_tab_model.py
from frameworks.wulf import Array, ViewModel
from resource_well.gui.impl.gen.view_models.views.lobby.resource_model import ResourceModel

class ResourcesTabModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(ResourcesTabModel, self).__init__(properties=properties, commands=commands)

    def getType(self):
        return self._getString(0)

    def setType(self, value):
        self._setString(0, value)

    def getResources(self):
        return self._getArray(1)

    def setResources(self, value):
        self._setArray(1, value)

    @staticmethod
    def getResourcesType():
        return ResourceModel

    def _initialize(self):
        super(ResourcesTabModel, self)._initialize()
        self._addStringProperty('type', '')
        self._addArrayProperty('resources', Array())
