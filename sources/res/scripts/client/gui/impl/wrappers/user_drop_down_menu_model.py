# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/wrappers/user_drop_down_menu_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/wrappers/user_drop_down_menu_model.py
from __future__ import absolute_import
import logging
from gui.impl.gen.view_models.ui_kit.drop_down_menu_item_model import DropDownMenuItemModel
from gui.impl.wrappers.user_list_model import UserListModel
_logger = logging.getLogger(__name__)

class UserDropDownMenuModel(UserListModel):
    __slots__ = ()

    def addItem(self, actionID, label, icon=None, isEnabled=True):
        item = DropDownMenuItemModel()
        item.setId(actionID)
        item.setLabel(label)
        item.setIsEnabled(isEnabled)
        if icon is not None:
            item.setIcon(icon)
        self.getItems().addViewModel(item)
        return

    def getItemByID(self, actionID):
        try:
            return next(item for item in self.getItems() if item.getId() == actionID)
        except StopIteration:
            _logger.error("Item with actionID '%d' is not found in drop down list", actionID)
            return

        return
