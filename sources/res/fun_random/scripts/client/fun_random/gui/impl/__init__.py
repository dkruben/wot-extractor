# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/impl/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/impl/__init__.py
from __future__ import absolute_import
from fun_random.gui.impl.gen.view_models.views.lobby.loadout.fun_random_loadout_constants import FunRandomLoadoutConstants
from gui.impl.lobby.tank_setup.backports.tooltips import ShellTooltipBuilder
from gui.impl.lobby.tank_setup.backports.tooltips import PANEL_SLOT_TOOLTIPS

def registerFunRandomImpl():
    PANEL_SLOT_TOOLTIPS.update({(FunRandomLoadoutConstants.FUN_RANDOM_CUSTOM_SHELLS): ShellTooltipBuilder})
