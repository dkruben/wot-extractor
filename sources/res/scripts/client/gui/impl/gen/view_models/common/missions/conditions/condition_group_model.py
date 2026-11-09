# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/common/missions/conditions/condition_group_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/missions/conditions/condition_group_model.py
from gui.impl.gen.view_models.common.missions.conditions.condition_base_model import ConditionBaseModel

class ConditionGroupModel(ConditionBaseModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(ConditionGroupModel, self).__init__(properties=properties, commands=commands)

    def getItems(self):
        return self._getArray(1)

    def setItems(self, value):
        self._setArray(1, value)

    def _initialize(self):
        super(ConditionGroupModel, self)._initialize()
        self._addArrayProperty('items')
