# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/dialogs/contents/multiple_items_content_to_upgrade.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/dialogs/contents/multiple_items_content_to_upgrade.py
import typing
from gui.impl.lobby.dialogs.contents.multiple_items_content import MultipleItemsContent
from gui.impl.lobby.dialogs.auxiliary.confirmed_items_packer import ConfirmedItemsToUpgradePacker
if typing.TYPE_CHECKING:
    from gui.impl.gen.view_models.views.lobby.common.multiple_items_content_model import MultipleItemsContentModel

class MultipleItemsContentToUpgrade(MultipleItemsContent):
    __slots__ = ()

    def __init__(self, viewModel, items, vehicleInvID=None, itemsType=None):
        super(MultipleItemsContentToUpgrade, self).__init__(viewModel, items, vehicleInvID, itemsType)
        self._confirmedItemsPacker = ConfirmedItemsToUpgradePacker(vehicleInvID=vehicleInvID)
