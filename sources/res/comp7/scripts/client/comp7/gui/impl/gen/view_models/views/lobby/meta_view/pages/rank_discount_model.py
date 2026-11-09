# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/meta_view/pages/rank_discount_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/meta_view/pages/rank_discount_model.py
from comp7.gui.impl.gen.view_models.views.lobby.progression_item_base_model import ProgressionItemBaseModel

class RankDiscountModel(ProgressionItemBaseModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(RankDiscountModel, self).__init__(properties=properties, commands=commands)

    def getValue(self):
        return self._getNumber(4)

    def setValue(self, value):
        self._setNumber(4, value)

    def getWasUnlocked(self):
        return self._getBool(5)

    def setWasUnlocked(self, value):
        self._setBool(5, value)

    def _initialize(self):
        super(RankDiscountModel, self)._initialize()
        self._addNumberProperty('value', 0)
        self._addBoolProperty('wasUnlocked', False)
