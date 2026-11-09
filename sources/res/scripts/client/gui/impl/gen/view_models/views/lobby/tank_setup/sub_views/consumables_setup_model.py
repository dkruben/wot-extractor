# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/sub_views/consumables_setup_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/sub_views/consumables_setup_model.py
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel

class ConsumablesSetupModel(BaseSetupModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=7):
        super(ConsumablesSetupModel, self).__init__(properties=properties, commands=commands)

    def getTempString(self):
        return self._getString(5)

    def setTempString(self, value):
        self._setString(5, value)

    def _initialize(self):
        super(ConsumablesSetupModel, self)._initialize()
        self._addStringProperty('tempString', '')
