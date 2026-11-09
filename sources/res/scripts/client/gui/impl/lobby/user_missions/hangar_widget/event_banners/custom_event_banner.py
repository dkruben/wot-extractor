# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/user_missions/hangar_widget/event_banners/custom_event_banner.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/user_missions/hangar_widget/event_banners/custom_event_banner.py
from __future__ import absolute_import
import typing
from gui.impl.lobby.user_missions.hangar_widget.event_banners.base_event_banner import BaseEventBanner
if typing.TYPE_CHECKING:
    from gui.impl.gen.view_models.views.lobby.user_missions.widget.event_banner_model import EventBannerModel

class CustomEventBanner(BaseEventBanner):

    @classmethod
    def getPluginPath(cls):
        raise NotImplementedError

    def fillModel(self, model):
        super(CustomEventBanner, self).fillModel(model)
        model.setPluginPath(self.getPluginPath())
