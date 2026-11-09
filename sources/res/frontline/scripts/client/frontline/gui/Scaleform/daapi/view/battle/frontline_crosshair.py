# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/frontline_crosshair.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/frontline_crosshair.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.battle.shared.crosshair import CrosshairPanelContainer
from gui.Scaleform.daapi.view.battle.shared.crosshair.plugins import AimDamagePlugin

class FrontlineAimDamagePlugin(AimDamagePlugin):

    def start(self):
        super(FrontlineAimDamagePlugin, self).start()
        componentSystem = self.sessionProvider.arenaVisitor.getComponentSystem()
        destructibleComponent = getattr(componentSystem, 'destructibleEntityComponent', None)
        if destructibleComponent is not None:
            destructibleComponent.onDestructibleEntityFeedbackReceived += self.__onDestructibleEntityFeedbackReceived
        return

    def stop(self):
        componentSystem = self.sessionProvider.arenaVisitor.getComponentSystem()
        destructibleComponent = getattr(componentSystem, 'destructibleEntityComponent', None)
        if destructibleComponent is not None:
            destructibleComponent.onDestructibleEntityFeedbackReceived -= self.__onDestructibleEntityFeedbackReceived
        return

    def __onDestructibleEntityFeedbackReceived(self, eventID, _, value):
        if eventID in self._DAMAGE_EVENTS:
            self._invalidateAimDamage(*value)


class FrontlineCrosshairPanelContainer(CrosshairPanelContainer):

    def _getPlugins(self):
        plugins = super(FrontlineCrosshairPanelContainer, self)._getPlugins()
        plugins['aimDamage'] = FrontlineAimDamagePlugin
        return plugins
