# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/collection/resources/local/cache.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/collection/resources/local/cache.py
import typing
from gui.collection import loggers
from gui.impl import backport
from gui.impl.gen import R
_logger = loggers.getLocalCacheLogger()
if typing.TYPE_CHECKING:
    from typing import Dict, List

class CollectionsLocalCacheMgr(object):
    __IMG = R.images.gui.maps.icons.collections.fakeCdn.images

    def startSync(self, *args, **kwargs):
        _logger.debug('Sync started')

    def stopSync(self, *args, **kwargs):
        _logger.debug('Sync stopped')

    def getImagesPaths(self, imagesIDs, callback=None):
        callback(True, self.__packImages(imagesIDs))

    def __packImages(self, imagesIDs):
        packed = {}
        for imageID in imagesIDs:
            group, sub, name = imageID.split('/')
            packed.setdefault(group, {})
            packed[group].setdefault(sub, {})
            resID = self.__IMG.dyn(group).dyn(sub).dyn(name)()
            if resID != R.invalid():
                packed[group][sub][name] = backport.image(resID)

        return packed
