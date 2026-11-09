# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/impl/gen/view_models/views/lobby/ext_ammo_panel_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/impl/gen/view_models/views/lobby/ext_ammo_panel_view.py
from gui.impl.gen.view_models.views.lobby.loadout.panel.ammunition.ammunition_panel_model import AmmunitionPanelModel

class ExtAmmoPanelView(AmmunitionPanelModel):
    __slots__ = ('onSwitch', )

    def __init__(self, properties=8, commands=3):
        super(ExtAmmoPanelView, self).__init__(properties=properties, commands=commands)

    def getAccelerationKeyName(self):
        return self._getString(6)

    def setAccelerationKeyName(self, value):
        self._setString(6, value)

    def getAccelerationIntCD(self):
        return self._getNumber(7)

    def setAccelerationIntCD(self, value):
        self._setNumber(7, value)

    def _initialize(self):
        super(ExtAmmoPanelView, self)._initialize()
        self._addStringProperty('accelerationKeyName', '')
        self._addNumberProperty('accelerationIntCD', 0)
        self.onSwitch = self._addCommand('onSwitch')
