# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/impl/gen/view_models/views/lobby/mission_progress_level_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/impl/gen/view_models/views/lobby/mission_progress_level_model.py
from story_mode.gui.impl.gen.view_models.views.lobby.progress_level_model import ProgressLevelModel

class MissionProgressLevelModel(ProgressLevelModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(MissionProgressLevelModel, self).__init__(properties=properties, commands=commands)

    def getTotal(self):
        return self._getNumber(4)

    def setTotal(self, value):
        self._setNumber(4, value)

    def _initialize(self):
        super(MissionProgressLevelModel, self)._initialize()
        self._addNumberProperty('total', 0)
