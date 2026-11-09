# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/tab_content.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/tab_content.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.meta.TabContentMeta import TabContentMeta
from gui.impl.battle.battle_page.tab_view import TabView
from gui.impl.gen import R

class TabContent(TabContentMeta):

    def _onPopulate(self):
        self._createInjectView()

    def _makeInjectView(self):
        self.__view = TabView(R.views.battle.battle_page.TabView())
        return self.__view

    def onTabChanged(self, tabAlias):
        self.__view.handleTabChange(tabAlias)
