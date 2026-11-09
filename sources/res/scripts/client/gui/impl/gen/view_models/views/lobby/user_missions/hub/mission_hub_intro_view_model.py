# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/user_missions/hub/mission_hub_intro_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/user_missions/hub/mission_hub_intro_view_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen import R

class MissionHubIntroViewModel(ViewModel):
    __slots__ = ('onClose', )

    def __init__(self, properties=4, commands=1):
        super(MissionHubIntroViewModel, self).__init__(properties=properties, commands=commands)

    def getHeader(self):
        return self._getResource(0)

    def setHeader(self, value):
        self._setResource(0, value)

    def getDescription(self):
        return self._getResource(1)

    def setDescription(self, value):
        self._setResource(1, value)

    def getButtonText(self):
        return self._getResource(2)

    def setButtonText(self, value):
        self._setResource(2, value)

    def getIcon(self):
        return self._getResource(3)

    def setIcon(self, value):
        self._setResource(3, value)

    def _initialize(self):
        super(MissionHubIntroViewModel, self)._initialize()
        self._addResourceProperty('header', R.invalid())
        self._addResourceProperty('description', R.invalid())
        self._addResourceProperty('buttonText', R.invalid())
        self._addResourceProperty('icon', R.invalid())
        self.onClose = self._addCommand('onClose')
