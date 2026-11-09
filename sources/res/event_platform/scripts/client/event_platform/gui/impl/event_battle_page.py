# wot-extractor: codigo DESCOMPILADO de sources/res/event_platform/scripts/client/event_platform/gui/impl/event_battle_page.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: event_platform/scripts/client/event_platform/gui/impl/event_battle_page.py
from __future__ import absolute_import
from debug_utils import LOG_ERROR
from gui.Scaleform.daapi.view.battle.classic import ClassicPage
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES

class EventBattlePage(ClassicPage):

    def __init__(self, components=None, external=None, fullStatsAlias=BATTLE_VIEW_ALIASES.FULL_STATS, **kwargs):
        LOG_ERROR('INIT --- EventBattlePage')
        super(EventBattlePage, self).__init__(components=components, external=external, fullStatsAlias=fullStatsAlias)
