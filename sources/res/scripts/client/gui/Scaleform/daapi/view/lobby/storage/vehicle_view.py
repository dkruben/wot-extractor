# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/storage/vehicle_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/storage/vehicle_view.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.lobby.storage.category_view import InventoryCategoryView
from gui.shared.gui_items import GUI_ITEM_TYPE

class VehicleView(InventoryCategoryView):

    def _populate(self):
        super(VehicleView, self)._populate()
        self._itemsCache.onSyncCompleted += self._onCacheResync

    def _dispose(self):
        self._itemsCache.onSyncCompleted -= self._onCacheResync
        super(VehicleView, self)._dispose()

    def _buildItems(self):
        pass

    def _getVO(self, item):
        pass

    def _getItemTypeID(self):
        return GUI_ITEM_TYPE.VEHICLE

    def _onCacheResync(self, *args):
        raise NotImplementedError
