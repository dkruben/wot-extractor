# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/AvatarInputHandler/keys_handlers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/AvatarInputHandler/keys_handlers.py
from __future__ import absolute_import
from future.utils import lrange
import CommandMapping
from helpers.dependency import replace_none_kwargs
from skeletons.gui.battle_session import IBattleSessionProvider

@replace_none_kwargs(guiSessionProvider=IBattleSessionProvider)
def processAmmoSelection(key, guiSessionProvider=None):
    if CommandMapping.g_instance.isFiredList(lrange(CommandMapping.CMD_AMMO_CHOICE_1, CommandMapping.CMD_AMMO_CHOICE_4), key):
        ammoCtrl = guiSessionProvider.shared.ammo
        if ammoCtrl:
            ammoCtrl.handleAmmoChoice(key)
        return True
    return
