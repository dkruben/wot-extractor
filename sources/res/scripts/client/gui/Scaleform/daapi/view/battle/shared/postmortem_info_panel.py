# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/postmortem_info_panel.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/postmortem_info_panel.py
from __future__ import absolute_import
from gui.impl.battle.postmortem_panel.postmortem_panel_view import PostmortemPanelView
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from gui.shared.system_factory import collectPostmortemInfoView
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class PostmortemInfoPanel(InjectComponentAdaptor):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def _makeInjectView(self, *args):
        arenaGuiType = self.__sessionProvider.arenaVisitor.getArenaGuiType()
        viewCls = collectPostmortemInfoView(arenaGuiType)
        infoPanelViewCls = viewCls if viewCls is not None else PostmortemPanelView
        self.__view = infoPanelViewCls()
        return self.__view
