# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/hangar/presenters/fun_random_mode_state_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/impl/lobby/hangar/presenters/fun_random_mode_state_presenter.py
from __future__ import absolute_import
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher, FunAssetPacksMixin
from fun_random.gui.feature.util.fun_wrappers import hasDesiredSubMode
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_mode_state_model import FunRandomModeStateModel
from gui.impl.pub.view_component import ViewComponent

class FunRandomModeStatePresenter(ViewComponent[FunRandomModeStateModel], FunAssetPacksMixin, FunSubModesWatcher):

    def __init__(self):
        super(FunRandomModeStatePresenter, self).__init__(model=FunRandomModeStateModel)

    @property
    def viewModel(self):
        return super(FunRandomModeStatePresenter, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(FunRandomModeStatePresenter, self)._onLoading(*args, **kwargs)
        self.startSubSettingsListening(self.__invalidateAll, desiredOnly=True)
        self.startSubSelectionListening(self.__invalidateAll)
        self.__invalidateAll()

    def _finalize(self):
        self.stopSubSelectionListening(self.__invalidateAll)
        self.stopSubSettingsListening(self.__invalidateAll, desiredOnly=True)
        super(FunRandomModeStatePresenter, self)._finalize()

    def _getCallbacks(self):
        return super(FunRandomModeStatePresenter, self)._getCallbacks() + (
         (
          'inventory.1', self.__invalidateAll),)

    @hasDesiredSubMode()
    def __invalidateAll(self, *_):
        with self.viewModel.transaction() as model:
            model.setAssetsPointer(self.getModeAssetsPointer())
            model.setSubModeAssetsPointer(self.getDesiredSubMode().getAssetsPointer())
            model.setHasSuitableVehicles(self.getDesiredSubMode().hasSuitableVehicles())
