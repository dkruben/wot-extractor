# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/post_progression/post_progression_cmp_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/post_progression/post_progression_cmp_view_model.py
from gui.impl.gen.view_models.views.lobby.post_progression.post_progression_base_view_model import PostProgressionBaseViewModel
from gui.impl.gen.view_models.views.lobby.post_progression.post_progression_compare_model import PostProgressionCompareModel

class PostProgressionCmpViewModel(PostProgressionBaseViewModel):
    __slots__ = ('onExitAction', )

    def __init__(self, properties=6, commands=2):
        super(PostProgressionCmpViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def compareControl(self):
        return self._getViewModel(5)

    @staticmethod
    def getCompareControlType():
        return PostProgressionCompareModel

    def _initialize(self):
        super(PostProgressionCmpViewModel, self)._initialize()
        self._addViewModelProperty('compareControl', PostProgressionCompareModel())
        self.onExitAction = self._addCommand('onExitAction')
