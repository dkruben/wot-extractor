# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/dialogs/sub_views/select_demount_kit_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/dialogs/sub_views/select_demount_kit_view_model.py
from gui.impl.gen.view_models.views.dialogs.sub_views.select_option_base_item_view_model import SelectOptionBaseItemViewModel

class SelectDemountKitViewModel(SelectOptionBaseItemViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(SelectDemountKitViewModel, self).__init__(properties=properties, commands=commands)

    def getStorageCount(self):
        return self._getNumber(4)

    def setStorageCount(self, value):
        self._setNumber(4, value)

    def getText(self):
        return self._getString(5)

    def setText(self, value):
        self._setString(5, value)

    def _initialize(self):
        super(SelectDemountKitViewModel, self)._initialize()
        self._addNumberProperty('storageCount', 0)
        self._addStringProperty('text', '')
