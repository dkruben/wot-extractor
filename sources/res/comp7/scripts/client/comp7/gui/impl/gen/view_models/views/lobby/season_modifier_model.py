# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/season_modifier_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/season_modifier_model.py
from frameworks.wulf import ViewModel

class SeasonModifierModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(SeasonModifierModel, self).__init__(properties=properties, commands=commands)

    def getEnabled(self):
        return self._getBool(0)

    def setEnabled(self, value):
        self._setBool(0, value)

    def _initialize(self):
        super(SeasonModifierModel, self)._initialize()
        self._addBoolProperty('enabled', False)
