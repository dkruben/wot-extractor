# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/battle/shared/clip/unlimited_clip_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/battle/shared/clip/unlimited_clip_presenter.py
from __future__ import absolute_import
import logging, typing
from gui.impl.gen.view_models.views.battle.shared.clip.unlimited_clip_model import UnlimitedClipModel
from gui.impl.pub.view_component import ViewComponent
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
if typing.TYPE_CHECKING:
    from gui.battle_control.controllers.consumables.ammo_ctrl import _GunSettings
_logger = logging.getLogger(__name__)

class UnlimitedClipPresenter(ViewComponent):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(UnlimitedClipPresenter, self).__init__(model=UnlimitedClipModel)

    @property
    def viewModel(self):
        return super(UnlimitedClipPresenter, self).getViewModel()

    def _initialize(self, *args, **kwargs):
        super(UnlimitedClipPresenter, self)._initialize(*args, **kwargs)
        ammoCtrl = self.__sessionProvider.shared.ammo
        if ammoCtrl is None:
            _logger.warning('UnlimitedClipPresenter: AmmoController is not available')
            return
        else:
            gunSettings = ammoCtrl.getGunSettings()
            if gunSettings is not None:
                self.__applyGunSettings(gunSettings)
            return

    def _getEvents(self):
        ammoCtrl = self.__sessionProvider.shared.ammo
        if ammoCtrl is None:
            _logger.warning('UnlimitedClipPresenter: AmmoController is not available')
            return ()
        else:
            return (
             (
              ammoCtrl.onGunSettingsSet, self.__onGunSettingsSet),)

    def __onGunSettingsSet(self, gunSettings):
        self.__applyGunSettings(gunSettings)

    def __applyGunSettings(self, gunSettings):
        with self.viewModel as model:
            model.setIsUnlimitedClip(gunSettings.isUnlimitedClip)
