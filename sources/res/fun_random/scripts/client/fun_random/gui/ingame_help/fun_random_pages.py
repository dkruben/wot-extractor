# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/ingame_help/fun_random_pages.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/ingame_help/fun_random_pages.py
from __future__ import absolute_import
from fun_random_common.fun_constants import ARENA_GUI_TYPE
from fun_random.gui.ingame_help import HelpPagePriority
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasBattleSubMode
from fun_random.gui.Scaleform.daapi.view.battle.hint_panel.hint_panel_plugin import HelpHintContext
from gui.impl import backport
from gui.ingame_help.detailed_help_pages import addPage, DetailedHelpPagesBuilder
from gui.shared.formatters import text_styles

class FunRandomHelpPagesBuilder(DetailedHelpPagesBuilder, FunSubModesWatcher):
    _SUITABLE_CTX_KEYS = ('isFunRandom', )

    @classmethod
    def isExclusive(cls):
        return cls.getBattleSubMode().getConfigurationModel().subMode.isExclusiveHelpPages

    @classmethod
    def priority(cls):
        return HelpPagePriority.FUN_RANDOM

    @classmethod
    @hasBattleSubMode(defReturn=())
    def buildPages(cls, _):
        pages = []
        battleSubMode = cls.getBattleSubMode()
        iconsRoot = battleSubMode.getIconsResRoot().battle_help
        localsRoot = battleSubMode.getLocalsResRoot()
        commonTitle = backport.text(localsRoot.detailsHelpTitle())
        for pageID, pageRes in sorted(localsRoot.detailsHelp.items()):
            addPage(pages, commonTitle, backport.text(pageRes.title()), text_styles.mainBig(backport.text(pageRes.description())), [], backport.image(iconsRoot.dyn(pageID)()), hintCtx=HelpHintContext.FUN_RANDOM)

        return pages

    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ctx['isFunRandom'] = arenaVisitor.getArenaGuiType() in ARENA_GUI_TYPE.FUN_RANDOM_RANGE
