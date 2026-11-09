# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/entitlements/entitlement_common.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/entitlements/entitlement_common.py
import typing
from helpers import dependency
if typing.TYPE_CHECKING:
    from typing import FrozenSet, Generator, Type
    from skeletons.gui.game_control import IEntitlementsConsumer
LOOT_BOX_COUNTER_ENTITLEMENT = 'loot_box_counter'
ENTITLEMENTS = (
 LOOT_BOX_COUNTER_ENTITLEMENT,)
_CONSUMERS = frozenset()

def iterConsumers():
    return (dependency.instance(iConsumer) for iConsumer in _CONSUMERS)
