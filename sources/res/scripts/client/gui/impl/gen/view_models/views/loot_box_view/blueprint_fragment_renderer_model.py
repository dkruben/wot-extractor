# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/loot_box_view/blueprint_fragment_renderer_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/loot_box_view/blueprint_fragment_renderer_model.py
from gui.impl.gen.view_models.views.loot_box_view.blueprint_congrats_model import BlueprintCongratsModel
from gui.impl.gen.view_models.views.loot_box_view.loot_def_renderer_model import LootDefRendererModel

class BlueprintFragmentRendererModel(LootDefRendererModel):
    __slots__ = ()

    def __init__(self, properties=14, commands=0):
        super(BlueprintFragmentRendererModel, self).__init__(properties=properties, commands=commands)

    @property
    def congratsViewModel(self):
        return self._getViewModel(13)

    @staticmethod
    def getCongratsViewModelType():
        return BlueprintCongratsModel

    def _initialize(self):
        super(BlueprintFragmentRendererModel, self)._initialize()
        self._addViewModelProperty('congratsViewModel', BlueprintCongratsModel())
