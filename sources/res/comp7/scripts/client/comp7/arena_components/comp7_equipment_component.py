# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/arena_components/comp7_equipment_component.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/arena_components/comp7_equipment_component.py
from __future__ import absolute_import
from comp7_core.arena_components.comp7_core_equipment_component import Comp7CoreEquipmentComponent, _AoeHealEffect
from helpers import dependency
from skeletons.gui.game_control import IComp7Controller

class _Comp7AoeHealEffect(_AoeHealEffect):
    __comp7Controller = dependency.descriptor(IComp7Controller)

    @property
    def _modeController(self):
        return self.__comp7Controller


class Comp7EquipmentComponent(Comp7CoreEquipmentComponent):
    _AOE_HEAL_EFFECT = _Comp7AoeHealEffect
