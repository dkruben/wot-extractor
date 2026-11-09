# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/post_progression/tooltip/setup_tooltip_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/post_progression/tooltip/setup_tooltip_view_model.py
from enum import Enum
from gui.impl.gen.view_models.views.lobby.post_progression.tooltip.feature_tooltip_view_model import FeatureTooltipViewModel

class SetupFeatureType(Enum):
    SHELLSCONSUMABLESSWITCH = 'shells_consumables_switch'
    OPTDEVBOOSTERSSWITCH = 'opt_dev_boosters_switch'


class SetupTooltipViewModel(FeatureTooltipViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(SetupTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def getIconName(self):
        return self._getString(3)

    def setIconName(self, value):
        self._setString(3, value)

    def getType(self):
        return SetupFeatureType(self._getString(4))

    def setType(self, value):
        self._setString(4, value.value)

    def getIsLevelShown(self):
        return self._getBool(5)

    def setIsLevelShown(self, value):
        self._setBool(5, value)

    def _initialize(self):
        super(SetupTooltipViewModel, self)._initialize()
        self._addStringProperty('iconName', '')
        self._addStringProperty('type')
        self._addBoolProperty('isLevelShown', True)
