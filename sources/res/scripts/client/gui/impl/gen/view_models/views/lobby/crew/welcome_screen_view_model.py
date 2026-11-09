# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/welcome_screen_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/welcome_screen_view_model.py
from frameworks.wulf import ViewModel

class WelcomeScreenViewModel(ViewModel):
    __slots__ = ('onClose', )

    def __init__(self, properties=0, commands=1):
        super(WelcomeScreenViewModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(WelcomeScreenViewModel, self)._initialize()
        self.onClose = self._addCommand('onClose')
