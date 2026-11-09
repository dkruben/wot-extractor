# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/game_loading/resources/cdn/images.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_loading/resources/cdn/images.py
import typing
from gui.game_loading import loggers
from gui.game_loading.resources.base import BaseResources
from gui.game_loading.resources.cdn.models import LocalSlideModel
from gui.game_loading.resources.cdn.cache import GameLoadingCdnCacheMgr
if typing.TYPE_CHECKING:
    from gui.game_loading.resources.cdn.models import CdnCacheDefaultsModel
_logger = loggers.getResourcesLogger()

class CdnImagesResources(BaseResources):
    __slots__ = ('_cdnCacheMgr', )

    def __init__(self, defaults):
        super(CdnImagesResources, self).__init__()
        self._cdnCacheMgr = GameLoadingCdnCacheMgr(defaults)

    def destroy(self):
        super(CdnImagesResources, self).destroy()
        self._cdnCacheMgr.destroy()

    def onConnected(self):
        self._cdnCacheMgr.onConnected()
        super(CdnImagesResources, self).onConnected()

    def onDisconnected(self):
        self._cdnCacheMgr.onDisconnected()
        super(CdnImagesResources, self).onDisconnected()

    def get(self):
        return self._cdnCacheMgr.nextSlide()
