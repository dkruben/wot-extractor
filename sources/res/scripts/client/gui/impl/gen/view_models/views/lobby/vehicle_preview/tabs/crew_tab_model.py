# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_preview/tabs/crew_tab_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_preview/tabs/crew_tab_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.vehicle_preview.tabs.tankman_preview_model import TankmanPreviewModel
from gui.impl.gen.view_models.views.lobby.vehicle_preview.tabs.title_model import TitleModel

class CrewTabModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(CrewTabModel, self).__init__(properties=properties, commands=commands)

    @property
    def headerModel(self):
        return self._getViewModel(0)

    @staticmethod
    def getHeaderModelType():
        return TitleModel

    def getIsLockedCrew(self):
        return self._getBool(1)

    def setIsLockedCrew(self, value):
        self._setBool(1, value)

    def getHasDog(self):
        return self._getBool(2)

    def setHasDog(self, value):
        self._setBool(2, value)

    def getNation(self):
        return self._getString(3)

    def setNation(self, value):
        self._setString(3, value)

    def getTankmen(self):
        return self._getArray(4)

    def setTankmen(self, value):
        self._setArray(4, value)

    @staticmethod
    def getTankmenType():
        return TankmanPreviewModel

    def _initialize(self):
        super(CrewTabModel, self)._initialize()
        self._addViewModelProperty('headerModel', TitleModel())
        self._addBoolProperty('isLockedCrew', False)
        self._addBoolProperty('hasDog', False)
        self._addStringProperty('nation', '')
        self._addArrayProperty('tankmen', Array())
