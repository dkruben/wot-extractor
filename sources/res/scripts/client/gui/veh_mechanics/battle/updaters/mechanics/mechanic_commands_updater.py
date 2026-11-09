# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/veh_mechanics/battle/updaters/mechanics/mechanic_commands_updater.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/veh_mechanics/battle/updaters/mechanics/mechanic_commands_updater.py
from __future__ import absolute_import
import typing
from events_handler import eventHandler
from gui.veh_mechanics.battle.updaters.mechanics.mechanics_common import VehicleMechanicUpdater

class VehicleMechanicCommandsUpdater(VehicleMechanicUpdater):

    @eventHandler
    def onMechanicComponentCatching(self, component):
        self.view.subscribeTo(component.commandsEvents)

    @eventHandler
    def onMechanicComponentReleasing(self, component):
        self.view.unsubscribeFrom(component.commandsEvents)
