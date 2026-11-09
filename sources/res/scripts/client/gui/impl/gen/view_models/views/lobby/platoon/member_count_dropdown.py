# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/platoon/member_count_dropdown.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/platoon/member_count_dropdown.py
from frameworks.wulf import Array
from gui.impl.gen.view_models.ui_kit.gf_drop_down_model import GfDropDownModel
from gui.impl.gen.view_models.views.lobby.platoon.dropdown_item import DropdownItem

class MemberCountDropdown(GfDropDownModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=1):
        super(MemberCountDropdown, self).__init__(properties=properties, commands=commands)

    def getItems(self):
        return self._getArray(3)

    def setItems(self, value):
        self._setArray(3, value)

    @staticmethod
    def getItemsType():
        return DropdownItem

    def getIsDisabled(self):
        return self._getBool(4)

    def setIsDisabled(self, value):
        self._setBool(4, value)

    def getTooltipText(self):
        return self._getString(5)

    def setTooltipText(self, value):
        self._setString(5, value)

    def _initialize(self):
        super(MemberCountDropdown, self)._initialize()
        self._addArrayProperty('items', Array())
        self._addBoolProperty('isDisabled', False)
        self._addStringProperty('tooltipText', '')
