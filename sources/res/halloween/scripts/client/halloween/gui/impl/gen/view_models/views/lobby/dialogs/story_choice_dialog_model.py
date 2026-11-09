# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/impl/gen/view_models/views/lobby/dialogs/story_choice_dialog_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/impl/gen/view_models/views/lobby/dialogs/story_choice_dialog_model.py
from halloween.gui.impl.gen.view_models.views.lobby.dialogs.hw_dialog_model import HwDialogModel

class StoryChoiceDialogModel(HwDialogModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=3):
        super(StoryChoiceDialogModel, self).__init__(properties=properties, commands=commands)

    def getChoice(self):
        return self._getString(0)

    def setChoice(self, value):
        self._setString(0, value)

    def _initialize(self):
        super(StoryChoiceDialogModel, self)._initialize()
        self._addStringProperty('choice', '')
