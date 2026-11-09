# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/quick_training/mentoring_license_component_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/quick_training/mentoring_license_component_model.py
from gui.impl.gen.view_models.views.lobby.crew.components.component_base_model import ComponentBaseModel

class MentoringLicenseComponentModel(ComponentBaseModel):
    __slots__ = ('openMentoring', )

    def __init__(self, properties=4, commands=1):
        super(MentoringLicenseComponentModel, self).__init__(properties=properties, commands=commands)

    def getAmount(self):
        return self._getNumber(1)

    def setAmount(self, value):
        self._setNumber(1, value)

    def getIsEnabled(self):
        return self._getBool(2)

    def setIsEnabled(self, value):
        self._setBool(2, value)

    def getIsVisible(self):
        return self._getBool(3)

    def setIsVisible(self, value):
        self._setBool(3, value)

    def _initialize(self):
        super(MentoringLicenseComponentModel, self)._initialize()
        self._addNumberProperty('amount', 0)
        self._addBoolProperty('isEnabled', False)
        self._addBoolProperty('isVisible', False)
        self.openMentoring = self._addCommand('openMentoring')
