# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/personal_missions_30/missions_categorizations_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/personal_missions_30/missions_categorizations_model.py
from gui.impl.gen.view_models.views.lobby.personal_missions_30.common.enums import MissionCategory
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.personal_missions_30.mission_model import MissionModel

class MissionsCategorizationsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(MissionsCategorizationsModel, self).__init__(properties=properties, commands=commands)

    def getMissionsCategory(self):
        return MissionCategory(self._getString(0))

    def setMissionsCategory(self, value):
        self._setString(0, value.value)

    def getMissions(self):
        return self._getArray(1)

    def setMissions(self, value):
        self._setArray(1, value)

    @staticmethod
    def getMissionsType():
        return MissionModel

    def _initialize(self):
        super(MissionsCategorizationsModel, self)._initialize()
        self._addStringProperty('missionsCategory')
        self._addArrayProperty('missions', Array())
