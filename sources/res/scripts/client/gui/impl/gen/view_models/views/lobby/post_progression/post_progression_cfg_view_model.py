# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/post_progression/post_progression_cfg_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/post_progression/post_progression_cfg_view_model.py
from gui.impl.gen.view_models.views.lobby.post_progression.post_progression_base_view_model import PostProgressionBaseViewModel
from gui.impl.gen.view_models.views.lobby.post_progression.post_progression_purchase_model import PostProgressionPurchaseModel

class PostProgressionCfgViewModel(PostProgressionBaseViewModel):
    __slots__ = ('onGoBackAction', 'onResearchAction')

    def __init__(self, properties=6, commands=3):
        super(PostProgressionCfgViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def purchasePreview(self):
        return self._getViewModel(5)

    @staticmethod
    def getPurchasePreviewType():
        return PostProgressionPurchaseModel

    def _initialize(self):
        super(PostProgressionCfgViewModel, self)._initialize()
        self._addViewModelProperty('purchasePreview', PostProgressionPurchaseModel())
        self.onGoBackAction = self._addCommand('onGoBackAction')
        self.onResearchAction = self._addCommand('onResearchAction')
