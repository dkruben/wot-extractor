# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/__init__.py
from __future__ import absolute_import
from gui.Scaleform.framework.entities.View import View

class LobbySubView(View):
    __background_alpha__ = 0.6

    def setEnvironment(self, app):
        app.setBackgroundAlpha(self.__background_alpha__)
        super(LobbySubView, self).setEnvironment(app)
