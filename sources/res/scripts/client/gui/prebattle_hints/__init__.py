# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/prebattle_hints/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prebattle_hints/__init__.py
from gui.prebattle_hints.controller import PrebattleHintsController
from gui.prebattle_hints.newbie_controller import NewbiePrebattleHintsController
from skeletons.gui.prebattle_hints.controller import IPrebattleHintsController
from skeletons.gui.prebattle_hints.newbie_controller import INewbiePrebattleHintsController

def controllersConfig(manager):
    manager.addInstance(IPrebattleHintsController, PrebattleHintsController(), finalizer='fini')
    manager.addInstance(INewbiePrebattleHintsController, NewbiePrebattleHintsController(), finalizer='fini')
