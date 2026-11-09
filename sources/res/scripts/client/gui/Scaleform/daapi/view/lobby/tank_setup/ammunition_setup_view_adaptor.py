# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/tank_setup/ammunition_setup_view_adaptor.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/tank_setup/ammunition_setup_view_adaptor.py
from __future__ import absolute_import
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from gui.impl.lobby.tank_setup.ammunition_setup.hangar import HangarAmmunitionSetupView
from gui.shared.system_factory import collectAmmunitionSetupView
from helpers import dependency
from skeletons.gui.game_control import IHangarGuiController

class AmmunitionSetupViewAdaptor(InjectComponentAdaptor):
    __hangarGuiCtrl = dependency.descriptor(IHangarGuiController)

    def __init__(self, ctx):
        super(AmmunitionSetupViewAdaptor, self).__init__()
        self.__ctx = ctx

    def _makeInjectView(self):
        currentPresetGetter = self.__hangarGuiCtrl.sfController.currentPresetGetter
        ammunitionPanelSetupCls = collectAmmunitionSetupView(currentPresetGetter.getAmmoSetupViewAlias())
        injectViewCls = ammunitionPanelSetupCls if ammunitionPanelSetupCls else HangarAmmunitionSetupView
        injectView = injectViewCls(**self.__ctx)
        self.__ctx = None
        return injectView
