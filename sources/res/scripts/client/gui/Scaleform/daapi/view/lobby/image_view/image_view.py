# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/image_view/image_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/image_view/image_view.py
from __future__ import absolute_import
from gui.impl.lobby.common.sound_constants import HANGAR_FILTERED_SOUND_SPACE
from gui.Scaleform.daapi.view.meta.ImageViewMeta import ImageViewMeta
_IMAGE_ROOT_PATH = '../maps/icons/imageView'

class ImageView(ImageViewMeta):
    _COMMON_SOUND_SPACE = HANGAR_FILTERED_SOUND_SPACE

    def __init__(self, ctx=None):
        super(ImageView, self).__init__(ctx)
        self.__image = ctx['img']

    def _populate(self):
        super(ImageView, self)._populate()
        self.setBgPath()

    def onClose(self):
        self.destroy()

    def setBgPath(self):
        image = ('').join((_IMAGE_ROOT_PATH, '/', self.__image))
        self.flashObject.as_setBgPath(image)
