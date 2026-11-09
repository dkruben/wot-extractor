# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/battle_modifiers_common/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/battle_modifiers_common/__init__.py
from __future__ import absolute_import
import pkgutil
from ExtensionsManager import g_extensionsManager
from battle_modifiers_common.battle_modifiers import BattleParams, ModifiersContext, ConstantsSet, ModifierScope, EXT_DATA_MODIFIERS_KEY, BATTLE_MODIFIERS_TYPE
if 'battle_modifiers' in [ext.name for ext in g_extensionsManager.activeExtensions] and pkgutil.find_loader('battle_modifiers_ext'):
    from battle_modifiers_ext.battle_modifiers import BattleModifiers, getDevGlobalModifiers
else:
    from battle_modifiers_common.battle_modifiers import BattleModifiers, getDevGlobalModifiers
__all__ = ('EXT_DATA_MODIFIERS_KEY', 'BATTLE_MODIFIERS_TYPE', 'BattleParams', 'ModifierScope',
           'BattleModifiers', 'ModifiersContext', 'getDevGlobalModifiers')
