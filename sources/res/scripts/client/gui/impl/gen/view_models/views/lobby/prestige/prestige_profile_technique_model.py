# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/prestige/prestige_profile_technique_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/prestige/prestige_profile_technique_model.py
from gui.impl.gen.view_models.views.lobby.prestige.prestige_base_model import PrestigeBaseModel
from gui.impl.gen.view_models.views.lobby.prestige.prestige_emblem_model import PrestigeEmblemModel

class PrestigeProfileTechniqueModel(PrestigeBaseModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(PrestigeProfileTechniqueModel, self).__init__(properties=properties, commands=commands)

    @property
    def nextEmblem(self):
        return self._getViewModel(3)

    @staticmethod
    def getNextEmblemType():
        return PrestigeEmblemModel

    def _initialize(self):
        super(PrestigeProfileTechniqueModel, self)._initialize()
        self._addViewModelProperty('nextEmblem', PrestigeEmblemModel())
