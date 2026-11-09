# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/battle_control/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/battle_control/__init__.py
from __future__ import absolute_import
from fun_random_common.fun_constants import ARENA_GUI_TYPE
from fun_random.gui.ingame_help.fun_random_pages import FunRandomHelpPagesBuilder
from fun_random.helpers.tips import FunRandomTipsCriteria
from gui.shared.system_factory import registerBattleTipCriteria, registerIngameHelpPagesBuilder

def registerFunRandomBattle():
    registerBattleTipCriteria(ARENA_GUI_TYPE.FUN_RANDOM, FunRandomTipsCriteria)
    registerIngameHelpPagesBuilder(FunRandomHelpPagesBuilder)
