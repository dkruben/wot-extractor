# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/gen/view_models/views/lobby/fort_rush_welcome_screen_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/impl/gen/view_models/views/lobby/fort_rush_welcome_screen_view_model.py
from frameworks.wulf import ViewModel

class FortRushWelcomeScreenViewModel(ViewModel):
    __slots__ = ('onVideoPlay', 'onClose', 'onViewLoaded')

    def __init__(self, properties=0, commands=3):
        super(FortRushWelcomeScreenViewModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(FortRushWelcomeScreenViewModel, self)._initialize()
        self.onVideoPlay = self._addCommand('onVideoPlay')
        self.onClose = self._addCommand('onClose')
        self.onViewLoaded = self._addCommand('onViewLoaded')
