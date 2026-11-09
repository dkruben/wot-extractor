# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/personal_reserves_tab.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/personal_reserves_tab.py
from __future__ import absolute_import
import logging
from gui.Scaleform.daapi.view.meta.PersonalReservesTabMeta import PersonalReservesTabMeta
from gui.impl.battle.battle_page.full_stats.personal_reserves_tab_view import PersonalReservesTabView
_logger = logging.getLogger(__name__)

class PersonalReservesTab(PersonalReservesTabMeta):

    def __init__(self):
        super(PersonalReservesTab, self).__init__()
        _logger.debug('[Personal Reserves Tab] init')

    def _onPopulate(self):
        _logger.debug('[Personal Reserves Tab] onPopulate')
        self._createInjectView()

    def _makeInjectView(self):
        _logger.debug('[Personal Reserves Tab] makeInjectView')
        self.__view = PersonalReservesTabView()
        return self.__view

    def onTabChanged(self, tabAlias):
        self.__view.handleTabChange(tabAlias)
