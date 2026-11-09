# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/views/sub_models/veh_skill_tree/alternate_configuration_dialog_loadout_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/views/sub_models/veh_skill_tree/alternate_configuration_dialog_loadout_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class LoadoutType(Enum):
    SHELLSCONSUMABLESSWITCH = 'shellsConsumablesSwitch'
    OPTDEVBOOSTERSSWITCH = 'optDevBoostersSwitch'


class AlternateConfigurationDialogLoadoutModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(AlternateConfigurationDialogLoadoutModel, self).__init__(properties=properties, commands=commands)

    def getType(self):
        return LoadoutType(self._getString(0))

    def setType(self, value):
        self._setString(0, value.value)

    def getIconName(self):
        return self._getString(1)

    def setIconName(self, value):
        self._setString(1, value)

    def getIsSelected(self):
        return self._getBool(2)

    def setIsSelected(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(AlternateConfigurationDialogLoadoutModel, self)._initialize()
        self._addStringProperty('type')
        self._addStringProperty('iconName', '')
        self._addBoolProperty('isSelected', False)
