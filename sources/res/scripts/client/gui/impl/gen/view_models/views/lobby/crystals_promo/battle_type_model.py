# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crystals_promo/battle_type_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crystals_promo/battle_type_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen import R
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.crystals_promo.condition_model import ConditionModel

class BattleTypeModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BattleTypeModel, self).__init__(properties=properties, commands=commands)

    @property
    def conditions(self):
        return self._getViewModel(0)

    @staticmethod
    def getConditionsType():
        return ConditionModel

    def getTitle(self):
        return self._getResource(1)

    def setTitle(self, value):
        self._setResource(1, value)

    def getIcon(self):
        return self._getResource(2)

    def setIcon(self, value):
        self._setResource(2, value)

    def _initialize(self):
        super(BattleTypeModel, self)._initialize()
        self._addViewModelProperty('conditions', UserListModel())
        self._addResourceProperty('title', R.invalid())
        self._addResourceProperty('icon', R.invalid())
