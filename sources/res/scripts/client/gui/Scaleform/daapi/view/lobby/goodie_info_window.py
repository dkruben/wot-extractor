# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/goodie_info_window.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/goodie_info_window.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.meta.GoodieInfoMeta import GoodieInfoMeta
from helpers import dependency
from skeletons.gui.goodies import IGoodiesCache

class GoodieInfoWindow(GoodieInfoMeta):
    goodiesCache = dependency.descriptor(IGoodiesCache)

    def __init__(self, ctx=None):
        super(GoodieInfoWindow, self).__init__()
        self.goodieID = ctx.get('goodieID')

    def onCancelClick(self):
        self.destroy()

    def onWindowClose(self):
        self.destroy()

    def _populate(self):
        super(GoodieInfoWindow, self)._populate()
        goodie = self.goodiesCache.getGoodie(self.goodieID)
        self.as_setInfoS({'windowTitle': (goodie.userName), 
           'name': (goodie.userName), 
           'icon': (goodie.iconInfo), 
           'description': (goodie.longDescription)})
