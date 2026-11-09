# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/battle/minimap/component.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/battle/minimap/component.py
from __future__ import absolute_import
import logging
from battle_royale.gui.Scaleform.daapi.view.battle.minimap import plugins
from gui.Scaleform.daapi.view.battle.epic.minimap import EpicMinimapComponent
_logger = logging.getLogger(__name__)

class BattleRoyaleMinimapComponent(EpicMinimapComponent):

    def _setupPlugins(self, arenaVisitor):
        setup = super(BattleRoyaleMinimapComponent, self)._setupPlugins(arenaVisitor)
        setup[plugins.PERSONAL_PLUGIN] = plugins.BattleRoyalePersonalEntriesPlugin
        setup[plugins.DEATH_ZONES_PLUGIN] = plugins.DeathZonesPlugin
        setup[plugins.RADAR_PLUGIN] = plugins.RadarPlugin
        setup[plugins.DETECTOR_PLUGIN] = plugins.DetectorPlugin
        setup[plugins.AIRDROP_PLUGIN] = plugins.AirDropPlugin
        setup[plugins.VEHICLES_PLUGIN] = plugins.BattleRoyaleVehiclePlugin
        setup[plugins.PINGING_PLUGIN] = plugins.BattleRoyalMinimapPingPlugin
        return setup
