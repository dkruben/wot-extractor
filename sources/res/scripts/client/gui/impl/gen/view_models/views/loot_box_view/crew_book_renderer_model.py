# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/loot_box_view/crew_book_renderer_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/loot_box_view/crew_book_renderer_model.py
from gui.impl.gen.view_models.views.loot_box_view.congrats_view_model import CongratsViewModel
from gui.impl.gen.view_models.views.loot_box_view.loot_animated_renderer_model import LootAnimatedRendererModel

class CrewBookRendererModel(LootAnimatedRendererModel):
    __slots__ = ()

    def __init__(self, properties=17, commands=0):
        super(CrewBookRendererModel, self).__init__(properties=properties, commands=commands)

    @property
    def congratsViewModel(self):
        return self._getViewModel(16)

    @staticmethod
    def getCongratsViewModelType():
        return CongratsViewModel

    def _initialize(self):
        super(CrewBookRendererModel, self)._initialize()
        self._addViewModelProperty('congratsViewModel', CongratsViewModel())
