# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/personal_missions_30/style_bonus_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/personal_missions_30/style_bonus_model.py
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

class StyleBonusModel(IconBonusModel):
    __slots__ = ()
    STYLE_3D_REWARD_NAME = 'style_3d'

    def __init__(self, properties=10, commands=0):
        super(StyleBonusModel, self).__init__(properties=properties, commands=commands)

    def getId(self):
        return self._getNumber(9)

    def setId(self, value):
        self._setNumber(9, value)

    def _initialize(self):
        super(StyleBonusModel, self)._initialize()
        self._addNumberProperty('id', 0)
