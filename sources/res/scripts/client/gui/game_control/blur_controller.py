# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/game_control/blur_controller.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_control/blur_controller.py
from __future__ import absolute_import
import logging
from gui.doc_loaders.blur_loader import readBlurSettings
from gui.shared.view_helpers.blur_manager import BlurManager, BlurEffect
from skeletons.gui.game_control import IBlurController
_logger = logging.getLogger(__name__)

class BlurController(IBlurController):

    def __init__(self):
        super(BlurController, self).__init__()
        self._settings = {}
        self._manager = None
        return

    def init(self):
        self._settings = readBlurSettings()
        self._manager = BlurManager()

    def fini(self):
        self._settings.clear()
        self._manager.fini()
        self._manager = None
        return

    def onAccountBecomeNonPlayer(self):
        self._manager.clear()

    def getSettingsByAlias(self, alias):
        settings = self._settings.get(alias)
        if settings is None:
            _logger.warning('No blur settings are defined for %s', alias)
            return
        else:
            return settings

    def createBlur(self, config):
        return BlurEffect(self._manager, config)
