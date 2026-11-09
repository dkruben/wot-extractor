# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/demount_kit/demount_kit_utils.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/demount_kit/demount_kit_utils.py
import typing
from gui.impl import backport
from gui.impl.gen import R
if typing.TYPE_CHECKING:
    from gui.shared.gui_items.artefacts import OptionalDevice

def getDemountDialogTitle(item, forFitting=False, fromSlot=False):
    titleRes = R.strings.demount_kit.equipmentDemountFromSlot if fromSlot else R.strings.demount_kit.equipmentDemount
    titleRes = titleRes.confirmationForFitting.title if forFitting else titleRes.confirmation.title
    return backport.text(titleRes(), equipment=item.userName)
