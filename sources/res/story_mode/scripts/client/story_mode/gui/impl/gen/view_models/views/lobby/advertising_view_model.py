# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/impl/gen/view_models/views/lobby/advertising_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/impl/gen/view_models/views/lobby/advertising_view_model.py
from frameworks.wulf import ViewModel

class AdvertisingViewModel(ViewModel):
    __slots__ = ('onClose', 'onSubmit')

    def __init__(self, properties=0, commands=2):
        super(AdvertisingViewModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(AdvertisingViewModel, self)._initialize()
        self.onClose = self._addCommand('onClose')
        self.onSubmit = self._addCommand('onSubmit')
