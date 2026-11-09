# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/cgf_components/vehicle_highlight.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/cgf_components/vehicle_highlight.py
from __future__ import absolute_import
import BigWorld, CGF, GenericComponents
from aih_constants import CTRL_MODES, CTRL_MODE_NAME
from constants import IS_CLIENT
if IS_CLIENT:
    from Avatar import PlayerAvatar
else:

    class PlayerAvatar(object):
        pass


class VehicleHighlightSystem(CGF.System):
    AvatarActivated = CGF.ActivateReaction(CGF.ReactRo(PlayerAvatar), CGF.Ro(GenericComponents.ControlModeStatus))
    AvatarDeactivated = CGF.DeactivateReaction(CGF.ReactRo(PlayerAvatar), CGF.Ro(GenericComponents.ControlModeStatus))
    Reactions = CGF.Reactions(AvatarActivated, AvatarDeactivated)

    def update(self):
        for _, controlModeStatus in self.reaction(self.AvatarDeactivated):
            self.onRemoved(controlModeStatus)

        for _, controlModeStatus in self.reaction(self.AvatarActivated):
            self.onAdded(controlModeStatus)

    def onAdded(self, controlModeStatus):
        if controlModeStatus.mode == CTRL_MODES.index(CTRL_MODE_NAME.VIDEO):
            BigWorld.wg_setHideEdges(True)

    def onRemoved(self, controlModeStatus):
        if controlModeStatus.mode == CTRL_MODES.index(CTRL_MODE_NAME.VIDEO):
            BigWorld.wg_setHideEdges(False)
