# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/tooltips/vehicle_params_note.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/tooltips/vehicle_params_note.py
from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen import R

class NoteThemeEnum(Enum):
    WARNING = 'warning'
    TEXTONLY = 'textOnly'
    CONTENT = 'content'
    AUTORELOADTIME = 'autoReloadTime'


class VehicleParamsNote(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(VehicleParamsNote, self).__init__(properties=properties, commands=commands)

    def getTitle(self):
        return self._getString(0)

    def setTitle(self, value):
        self._setString(0, value)

    def getIcon(self):
        return self._getResource(1)

    def setIcon(self, value):
        self._setResource(1, value)

    def getTheme(self):
        return NoteThemeEnum(self._getString(2))

    def setTheme(self, value):
        self._setString(2, value.value)

    def _initialize(self):
        super(VehicleParamsNote, self)._initialize()
        self._addStringProperty('title', '')
        self._addResourceProperty('icon', R.invalid())
        self._addStringProperty('theme')
