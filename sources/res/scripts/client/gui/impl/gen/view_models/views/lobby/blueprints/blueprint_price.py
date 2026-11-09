# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/blueprints/blueprint_price.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/blueprints/blueprint_price.py
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.blueprints.blueprint_value_price import BlueprintValuePrice

class BlueprintPrice(BlueprintValuePrice):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(BlueprintPrice, self).__init__(properties=properties, commands=commands)

    def getIconBig(self):
        return self._getResource(7)

    def setIconBig(self, value):
        self._setResource(7, value)

    def getNationName(self):
        return self._getString(8)

    def setNationName(self, value):
        self._setString(8, value)

    def getValue(self):
        return self._getNumber(9)

    def setValue(self, value):
        self._setNumber(9, value)

    def _initialize(self):
        super(BlueprintPrice, self)._initialize()
        self._addResourceProperty('iconBig', R.invalid())
        self._addStringProperty('nationName', '')
        self._addNumberProperty('value', 0)
