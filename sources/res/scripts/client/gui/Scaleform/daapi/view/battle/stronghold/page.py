# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/stronghold/page.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/stronghold/page.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.battle.classic import ClassicPage
from gui.Scaleform.daapi.view.battle.shared.crosshair import CrosshairPanelContainer
from gui.Scaleform.daapi.view.battle.shared.markers2d.manager import KillCamMarkersManager
from gui.Scaleform.daapi.view.battle.stronghold.manager import StrongholdMarkersManager
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES
_STRONGHOLD_EXTERNAL_COMPONENTS = (
 CrosshairPanelContainer, StrongholdMarkersManager, KillCamMarkersManager)

class StrongholdPage(ClassicPage):

    def __init__(self, components=None, external=_STRONGHOLD_EXTERNAL_COMPONENTS, fullStatsAlias=BATTLE_VIEW_ALIASES.FULL_STATS, **kwargs):
        super(StrongholdPage, self).__init__(components=components, external=external, fullStatsAlias=fullStatsAlias)
        self.__soundControl = None
        return
