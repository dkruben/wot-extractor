# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicles/mechanics/mechanic_inputs/mechanic_single_input.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicles/mechanics/mechanic_inputs/mechanic_single_input.py
from __future__ import absolute_import
from vehicles.mechanics.mechanic_inputs.mechanic_base_input import BaseMechanicInput
from vehicles.mechanics.mechanic_inputs.mechanic_input_profile import MechanicInputProfile

class MechanicSingleInput(BaseMechanicInput):

    def __init__(self, component, profileName, actionName, inputCallback):
        super(MechanicSingleInput, self).__init__()
        self._register(MechanicInputProfile(component.entity, profileName, actionName, inputCallback))
