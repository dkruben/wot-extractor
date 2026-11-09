# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/ingame_help/detailed_help_pages.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/ingame_help/detailed_help_pages.py
from __future__ import absolute_import
from comp7_core.gui.ingame_help.detailed_help_pages import Comp7CorePagesBuilder
from comp7_common.comp7_constants import ARENA_GUI_TYPE
from comp7.gui.ingame_help import HelpPagePriority
from gui.impl.gen import R

class Comp7PagesBuilder(Comp7CorePagesBuilder):
    _SUITABLE_CTX_KEYS = ('isComp7', )
    _PAGE_NAMES = ('seasonModifiers', 'poi', 'roleSkills', 'nightMaps', 'rules')
    _MODE_RES_ROOT_TEXTS = R.strings.ingame_help.detailsHelp.comp7
    _MODE_RES_ROOT_IMAGES = R.images.comp7.gui.maps.icons.battleHelp

    @classmethod
    def priority(cls):
        return HelpPagePriority.COMP7

    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ctx['isComp7'] = arenaVisitor.getArenaGuiType() in ARENA_GUI_TYPE.COMP7_RANGE
