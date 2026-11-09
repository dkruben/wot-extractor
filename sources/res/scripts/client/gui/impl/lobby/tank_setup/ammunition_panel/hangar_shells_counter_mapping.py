# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/tank_setup/ammunition_panel/hangar_shells_counter_mapping.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tank_setup/ammunition_panel/hangar_shells_counter_mapping.py
from account_helpers.settings_core.ServerSettingsManager import UI_STORAGE_KEYS

class ShellCounterMapping(dict):

    def __init__(self, vehicle):
        super(ShellCounterMapping, self).__init__({(vehicle.gun.isDamageMutable): (UI_STORAGE_KEYS.MUTABLE_DAMAGE_SHELL_MARK_IS_SHOWN), 
           (vehicle.gun.isNonPiercingDamage): (UI_STORAGE_KEYS.AUTO_SHOT_NPD_SHELLS_MARK_IS_SHOWN)})
