# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/web/web_client_api/hero_tank/vehicle.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/hero_tank/vehicle.py
from __future__ import absolute_import
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.shared import event_dispatcher
from helpers import dependency
from skeletons.gui.game_control import IHeroTankController
from web.web_client_api import w2c, W2CSchema

class HeroTankWebApiMixin(object):
    __heroControl = dependency.descriptor(IHeroTankController)

    @w2c(W2CSchema, 'get_id')
    def getName(self, _):
        return self.__heroControl.getCurrentTankCD()

    @w2c(W2CSchema, 'show_preview')
    def showPreview(self, _):
        tankCd = self.__heroControl.getCurrentTankCD()
        if tankCd:
            event_dispatcher.goToHeroTankOnScene(tankCd, previewAlias=VIEW_ALIAS.LOBBY_STORE)
