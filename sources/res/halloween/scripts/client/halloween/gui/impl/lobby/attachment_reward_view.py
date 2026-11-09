# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/attachment_reward_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/impl/lobby/attachment_reward_view.py
from __future__ import absolute_import
from frameworks.wulf import WindowFlags, WindowLayer
from gui.impl.gen import R
from gui.impl.lobby.customization.customization_rarity_reward_screen.customization_rarity_reward_screen import CustomizationRarityRewardScreen
from gui.impl.pub.lobby_window import LobbyNotificationWindow
from gui.shared.view_helpers.blur_manager import CachedBlur
from halloween.gui.impl.gen.view_models.views.lobby.attachments_view import AttachmentsView
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController
from helpers import dependency

class AttachmentRewardView(CustomizationRarityRewardScreen):
    _LAYOUT_ID = R.views.halloween.mono.lobby.attachments_reward_view()
    _MODEL = AttachmentsView
    _hwArtefactsCtrl = dependency.descriptor(IHalloweenArtefactsController)

    def _onLoading(self, *args, **kwargs):
        super(AttachmentRewardView, self)._onLoading(*args, **kwargs)
        self.viewModel.setHasNextScreen(self._hwArtefactsCtrl.isProgressCompleted())


class AttachmentRewardWindow(LobbyNotificationWindow):
    __slots__ = ('_blur', '_args')

    def __init__(self, element, isFirstEntry):
        self._blur = None
        super(AttachmentRewardWindow, self).__init__(wndFlags=WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, content=AttachmentRewardView(element, isFirstEntry), layer=WindowLayer.OVERLAY)
        self._args = (
         element, isFirstEntry)
        return

    def isParamsEqual(self, *args):
        return self._args == args

    def _initialize(self):
        super(AttachmentRewardWindow, self)._initialize()
        self._blur = CachedBlur(enabled=True, ownLayer=self.layer - 1)

    def _finalize(self):
        self._blur.fini()
        self._blur = None
        super(AttachmentRewardWindow, self)._finalize()
        return
