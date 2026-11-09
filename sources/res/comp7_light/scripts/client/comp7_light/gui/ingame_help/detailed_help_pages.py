# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/ingame_help/detailed_help_pages.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/ingame_help/detailed_help_pages.py
from __future__ import absolute_import
from gui.impl.gen import R
from comp7_core.gui.ingame_help.detailed_help_pages import Comp7CorePagesBuilder
from comp7_light_constants import ARENA_GUI_TYPE
from comp7_light.gui.ingame_help import HelpPagePriority

class Comp7LightPagesBuilder(Comp7CorePagesBuilder):
    _SUITABLE_CTX_KEYS = ('isComp7Light', )
    _MODE_RES_ROOT_TEXTS = R.strings.ingame_help.detailsHelp.comp7Light
    _MODE_RES_ROOT_IMAGES = R.images.comp7_light.gui.maps.icons.battleHelp

    @classmethod
    def priority(cls):
        return HelpPagePriority.COMP7_LIGHT

    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ctx['isComp7Light'] = arenaVisitor.getArenaGuiType() == ARENA_GUI_TYPE.COMP7_LIGHT
