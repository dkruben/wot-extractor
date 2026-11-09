# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/cgf_components/rechargeable_nitro_components.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/cgf_components/rechargeable_nitro_components.py
from __future__ import absolute_import
import CGF, SoundGroups
from cgf_script.registration import registerComponent, ComponentProperty
from constants import IS_CLIENT
if IS_CLIENT:
    from RechargeableNitroController import RechargeableNitroController
else:

    class RechargeableNitroController(object):
        pass


@registerComponent
class RechargeableNitroRTPCComponent(object):
    category = 'Sound'
    editorTitle = 'Rechargeable Nitro RTPC'
    domain = CGF.Domain.Client
    RTPCName = ComponentProperty(type=CGF.PropertyType.String, value='RTPC_ext_abl_nitro_fuel', editorName='RTPC name')

    def __init__(self):
        super(RechargeableNitroRTPCComponent, self).__init__()
        self.rechargeableNitroControllerGO = None
        self.progress = -1.0
        return


class RechargeableNitroMechanicSystem(CGF.System):
    NitroActivated = CGF.ActivateReaction(CGF.GameObject, CGF.ReactRw(RechargeableNitroRTPCComponent))
    NitroDeactivated = CGF.DeactivateReaction(CGF.ReactRw(RechargeableNitroRTPCComponent))
    NitroIterate = CGF.IterateReaction(CGF.ActiveOnly, CGF.Rw(RechargeableNitroRTPCComponent))
    NitroControllerAccess = CGF.AccessReaction(CGF.GameObject, CGF.Rw(RechargeableNitroController))
    Reactions = CGF.Reactions(NitroActivated, NitroDeactivated, NitroIterate, NitroControllerAccess)

    def commonUpdate(self):
        nitroAccess = self.reaction(self.NitroControllerAccess)
        for nitro in self.reaction(self.NitroDeactivated):
            nitro.rechargeableNitroControllerGO = None
            self.__setRechargeableNitroRTPC(nitro)

        for go, nitro in self.reaction(self.NitroActivated):
            nitro.rechargeableNitroControllerGO, _ = CGF.findParentWithReaction(go, nitroAccess)
            self.__setRechargeableNitroRTPC(nitro)

        return

    def periodUpdate(self):
        for nitro in self.reaction(self.NitroIterate):
            self.__setRechargeableNitroRTPC(nitro)

    def __setRechargeableNitroRTPC(self, rechargeableNitroRTPCComponent):
        progress = 0.0
        if rechargeableNitroRTPCComponent.rechargeableNitroControllerGO is not None:
            progress = self.__getRechargeableNitroActiveProgress(rechargeableNitroRTPCComponent.rechargeableNitroControllerGO)
        if rechargeableNitroRTPCComponent.progress != progress:
            SoundGroups.g_instance.setGlobalRTPC(rechargeableNitroRTPCComponent.RTPCName, progress)
            rechargeableNitroRTPCComponent.progress = progress
        return

    def __getRechargeableNitroActiveProgress(self, rechargeableNitroControllerGO):
        nitroAccess = self.reaction(self.NitroControllerAccess)
        _, rechargeableNitroController = nitroAccess.find(rechargeableNitroControllerGO)
        if not rechargeableNitroController:
            return 0.0
        return 100 * (1 - rechargeableNitroController.getMechanicState().progress)
