# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/impl/gen/view_models/views/lobby/attachments_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/impl/gen/view_models/views/lobby/attachments_view.py
from gui.impl.gen.view_models.views.lobby.customization.customization_rarity_reward_screen_model import CustomizationRarityRewardScreenModel

class AttachmentsView(CustomizationRarityRewardScreenModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=2):
        super(AttachmentsView, self).__init__(properties=properties, commands=commands)

    def getHasNextScreen(self):
        return self._getBool(5)

    def setHasNextScreen(self, value):
        self._setBool(5, value)

    def _initialize(self):
        super(AttachmentsView, self)._initialize()
        self._addBoolProperty('hasNextScreen', False)
