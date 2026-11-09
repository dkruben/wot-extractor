# wot-extractor: codigo DESCOMPILADO de sources/res/resource_well/scripts/client/resource_well_personality.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: resource_well/scripts/client/resource_well_personality.py
from __future__ import absolute_import
from gui.impl.lobby.user_missions.hangar_widget.event_banners.event_banners_container import EventBannersContainer
from gui.shared.system_factory import registerAwardControllerHandlers
from gui.shared.system_factory import registerBannerEntryPointValidator
from resource_well.gui.Scaleform import registerResourceWellScaleform
from resource_well.gui.game_control import registerResourceWellController
from resource_well.gui.game_control.award_controller_handlers import ResourceWellRewardHandler
from resource_well.gui.impl.lobby.feature.event_banner import ResourceWellEventBanner, isResourceWellEventBannerAvailable
from resource_well.messenger import registerResourceWellMessengerFormatter
from resource_well.notification import registerResourceWellNotifications
from resource_well.web.resource_well_w2c import registerResourceWellOpenTabWebApi

def preInit():
    registerResourceWellController()
    registerResourceWellScaleform()
    registerAwardControllerHandlers((ResourceWellRewardHandler,))
    registerResourceWellNotifications()
    registerResourceWellMessengerFormatter()
    registerResourceWellOpenTabWebApi()
    EventBannersContainer().registerEventBanner(ResourceWellEventBanner)
    registerBannerEntryPointValidator(ResourceWellEventBanner.NAME, isResourceWellEventBannerAvailable)


def init():
    pass


def start():
    pass


def fini():
    pass
