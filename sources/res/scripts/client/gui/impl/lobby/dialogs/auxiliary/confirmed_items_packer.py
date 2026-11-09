# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/dialogs/auxiliary/confirmed_items_packer.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/dialogs/auxiliary/confirmed_items_packer.py
import typing
from gui.impl.lobby.dialogs.auxiliary.confirmed_item import ConfirmedItem
from gui.impl.lobby.dialogs.auxiliary.confirmed_item_to_upgrade import ConfirmedItemToUpgrade
if typing.TYPE_CHECKING:
    from gui.shared.gui_items.fitting_item import FittingItem
    from typing import Iterable, Dict, Callable, Set, Tuple

class ConfirmedItemsPacker(object):

    def __init__(self, **kwargs):
        self._ctx = kwargs

    def packItemsType(self, items, typesToCombine=None):
        if typesToCombine is not None:
            return set(next((typesToCombine[t] for t in typesToCombine if item.itemTypeID in t), item.itemTypeName) for item in items)
        else:
            return set(item.itemTypeName for item in items)

    def packItems(self, items, filterFunc=None, sortFunction=None):
        itemClass = self._getItemClass()
        if callable(sortFunction):
            return sorted([itemClass.createFromGUIItem(i, self._ctx) for i in items if filterFunc is not None and not filterFunc(i) or filterFunc is None], cmp=sortFunction)
        else:
            return [itemClass.createFromGUIItem(i, self._ctx) for i in items if filterFunc is not None and not filterFunc(i) or filterFunc is None]

    @classmethod
    def _getItemClass(cls):
        return ConfirmedItem


class ConfirmedItemsToUpgradePacker(ConfirmedItemsPacker):

    @classmethod
    def _getItemClass(cls):
        return ConfirmedItemToUpgrade
