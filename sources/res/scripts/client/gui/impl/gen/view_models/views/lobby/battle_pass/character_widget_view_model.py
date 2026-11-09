# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/character_widget_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/character_widget_view_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.character_model import CharacterModel

class CharacterWidgetViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(CharacterWidgetViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def free(self):
        return self._getViewModel(0)

    @staticmethod
    def getFreeType():
        return CharacterModel

    @property
    def paid(self):
        return self._getViewModel(1)

    @staticmethod
    def getPaidType():
        return CharacterModel

    def _initialize(self):
        super(CharacterWidgetViewModel, self)._initialize()
        self._addViewModelProperty('free', CharacterModel())
        self._addViewModelProperty('paid', CharacterModel())
