# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/common/tutorial/enabled_effect_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/tutorial/enabled_effect_model.py
from gui.impl.gen.view_models.common.tutorial.effect_model import EffectModel

class EnabledEffectModel(EffectModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(EnabledEffectModel, self).__init__(properties=properties, commands=commands)

    def getEnabled(self):
        return self._getBool(4)

    def setEnabled(self, value):
        self._setBool(4, value)

    def _initialize(self):
        super(EnabledEffectModel, self)._initialize()
        self._addBoolProperty('enabled', False)
