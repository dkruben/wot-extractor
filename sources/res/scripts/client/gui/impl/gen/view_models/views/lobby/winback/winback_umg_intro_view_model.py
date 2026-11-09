# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/winback/winback_umg_intro_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/winback/winback_umg_intro_view_model.py
from frameworks.wulf import ViewModel

class WinbackUmgIntroViewModel(ViewModel):
    __slots__ = ('onClose', )

    def __init__(self, properties=3, commands=1):
        super(WinbackUmgIntroViewModel, self).__init__(properties=properties, commands=commands)

    def getHasBattlePass(self):
        return self._getBool(0)

    def setHasBattlePass(self, value):
        self._setBool(0, value)

    def getBackgroundPlugin(self):
        return self._getString(1)

    def setBackgroundPlugin(self, value):
        self._setString(1, value)

    def getDailyQuestsPlugin(self):
        return self._getString(2)

    def setDailyQuestsPlugin(self, value):
        self._setString(2, value)

    def _initialize(self):
        super(WinbackUmgIntroViewModel, self)._initialize()
        self._addBoolProperty('hasBattlePass', False)
        self._addStringProperty('backgroundPlugin', '')
        self._addStringProperty('dailyQuestsPlugin', '')
        self.onClose = self._addCommand('onClose')
