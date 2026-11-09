# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/image_helper.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/image_helper.py
from __future__ import absolute_import
from future.utils import viewitems, viewvalues
import BigWorld, ResMgr
from adisp import adisp_async
from constants import GF_RES_PROTOCOL
from debug_utils import LOG_WARNING, LOG_ERROR
from gui.shared.utils import mapTextureToTheMemory, getImageSize, removeTextureFromMemory

def readLocalImage(path):
    data = ResMgr.openSection(path)
    if data is not None:
        return data.asBinary
    else:
        return


def getTextureLinkByID(imageID, prefix=GF_RES_PROTOCOL.IMG):
    return ('{}{}').format(prefix, imageID)


class ImageHelper(object):

    @staticmethod
    def getMemoryTexturePath(image, temp=True):
        return mapTextureToTheMemory(image, temp=temp)

    @staticmethod
    def removeTextureFromMemory(textureID):
        removeTextureFromMemory(textureID)

    @staticmethod
    def requestImageByUrl(url, callback, size=None, defaultGetter=None):
        defaultGetter = defaultGetter or (lambda v: None)

        def _onImageReceived(_, img):
            if size:
                imgSize = getImageSize(img)
                if imgSize != size:
                    LOG_WARNING('Received image has invalid size, use default instead', imgSize, size, url, type(img))
                    img = defaultGetter(size)
            callback(img)

        if hasattr(BigWorld.player(), 'customFilesCache'):
            if url is not None:
                BigWorld.player().customFilesCache.get(url, _onImageReceived)
            else:
                BigWorld.callback(0.0, (lambda : callback(defaultGetter(size))))
        else:
            LOG_WARNING('Trying to get image by url from non-account', url)
            BigWorld.callback(0.0, (lambda : callback(defaultGetter(size))))
        return


class ImagesFetchCoordinator(object):

    def __init__(self):
        self.__texturesCache = {}
        self.__isDying = False

    def __del__(self):
        for url, imageID in viewitems(self.__texturesCache):
            LOG_ERROR(('Image "{}" was not removed from memory (id={}). Perhaps, forgot to call "fini"').format(url, imageID))

    @adisp_async
    def fetchImageByUrl(self, url, oneUse=True, callback=None):
        if self.__isDying:
            callback(None)
        elif url in self.__texturesCache:
            callback(getTextureLinkByID(self.__texturesCache[url]))
        else:

            def onImageData(imageData):
                if imageData and not self.__isDying:
                    imageID = mapTextureToTheMemory(imageData, temp=oneUse)
                    if not oneUse:
                        self.__texturesCache[url] = imageID
                    callback(getTextureLinkByID(imageID))
                    return
                else:
                    callback(None)
                    return

            ImageHelper.requestImageByUrl(url, onImageData)
        return

    def clearMappedImageByUrl(self, url):
        if url not in self.__texturesCache:
            LOG_WARNING(('Mapped image "{}" not found!').format(url))
        else:
            removeTextureFromMemory(self.__texturesCache[url])

    def clearAllMappedImages(self):
        for imageID in viewvalues(self.__texturesCache):
            removeTextureFromMemory(imageID)

        self.__texturesCache.clear()

    def fini(self):
        self.clearAllMappedImages()
        self.__isDying = True
