# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/web/web_client_api/ui/maps_training.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/ui/maps_training.py
from __future__ import absolute_import
from helpers import dependency
from skeletons.gui.game_control import IMapsTrainingController
from web.web_client_api import w2c, W2CSchema

class OpenMapsTrainingMixin(object):
    mapsTrainingController = dependency.descriptor(IMapsTrainingController)

    @w2c(W2CSchema, 'maps_training')
    def selectMapsTrainingMode(self, _):
        if self.mapsTrainingController.isMapsTrainingEnabled:
            self.mapsTrainingController.selectMapsTrainingMode()
