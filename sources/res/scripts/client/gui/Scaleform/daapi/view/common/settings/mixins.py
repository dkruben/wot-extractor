# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/common/settings/mixins.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/common/settings/mixins.py
from __future__ import absolute_import
import typing
from frameworks.wulf import WindowLayer
if typing.TYPE_CHECKING:
    from gui.Scaleform.framework.managers import ContainerManager
_LAYERS = [
 WindowLayer.FULLSCREEN_WINDOW, WindowLayer.CURSOR, WindowLayer.WAITING, WindowLayer.SERVICE_LAYOUT]

class LayerVisibilityMixin(object):

    def __init__(self, *args, **kwargs):
        super(LayerVisibilityMixin, self).__init__(*args, **kwargs)
        self.__previouslyVisibleLayers = None
        return

    def _populate(self):
        super(LayerVisibilityMixin, self)._populate()
        containerManager = self.app.containerManager
        self.__previouslyVisibleLayers = containerManager.getVisibleLayers()
        containerManager.setVisibleLayers(_LAYERS)

    def _dispose(self):
        super(LayerVisibilityMixin, self)._dispose()
        containerManager = self.app.containerManager
        containerManager.setVisibleLayers(self.__previouslyVisibleLayers)
        self.__previouslyVisibleLayers = None
        return
