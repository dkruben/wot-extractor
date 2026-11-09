# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicles/mechanics/generic_mechanics/spec_boost_mode/mechanic_interfaces.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicles/mechanics/generic_mechanics/spec_boost_mode/mechanic_interfaces.py
from __future__ import absolute_import
import typing
from vehicles.mechanics.common.mechanic_interfaces import IMechanicWithVariants
from vehicles.mechanics.mechanic_states import IMechanicState
if typing.TYPE_CHECKING:
    from items.components.shared_components import SpecBoostModeParams

class ISpecBoostModeMechanicParams(IMechanicWithVariants):

    @classmethod
    def fromMechanicParams(cls, params):
        raise NotImplementedError


class ISpecBoostModeMechanicState(IMechanicState):

    @classmethod
    def fromComponentStatus(cls, status):
        raise NotImplementedError

    @property
    def progress(self):
        raise NotImplementedError

    @property
    def timeLeft(self):
        raise NotImplementedError

    @property
    def state(self):
        raise NotImplementedError
