# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/platoon/dropdown_item.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/platoon/dropdown_item.py
from gui.impl.gen.view_models.ui_kit.gf_drop_down_item import GfDropDownItem
from gui.impl.gen.view_models.views.lobby.platoon.dropdown_item_meta import DropdownItemMeta

class DropdownItem(GfDropDownItem):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(DropdownItem, self).__init__(properties=properties, commands=commands)

    @property
    def meta(self):
        return self._getViewModel(3)

    @staticmethod
    def getMetaType():
        return DropdownItemMeta

    def _initialize(self):
        super(DropdownItem, self)._initialize()
        self._addViewModelProperty('meta', DropdownItemMeta())
