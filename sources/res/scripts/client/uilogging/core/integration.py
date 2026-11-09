# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/uilogging/core/integration.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/core/integration.py
from __future__ import absolute_import
import json, logging, typing
from gui.impl.gen.view_models.common.ui_logger_model import UiLoggerModel
from helpers import dependency
from skeletons.gui.impl import IGuiLoader
from skeletons.ui_logging import IUILoggingCore, IUILoggingListener
from wotdecorators import noexcept
_logger = logging.getLogger(__name__)

class UILoggingListener(IUILoggingListener):
    _core = dependency.descriptor(IUILoggingCore)
    __slots__ = ('__model', )

    def __init__(self):
        super(UILoggingListener, self).__init__()
        guiLoader = dependency.instance(IGuiLoader)
        self.__model = typing.cast(UiLoggerModel, guiLoader.uiLogger.getModel())
        self.__model.log += self._log

    def fini(self):
        if self.__model is not None:
            self.__model.log -= self._log
            _logger.debug('UIGFLoggingListener unsubscribed from model.')
        self.__model = None
        _logger.debug('UIGFLoggingListener destroyed.')
        return

    @noexcept
    def _log(self, args):
        self._core.log(feature=args['feature'], group=args['group'], action=args['action'], loglevel=args['logLevel'], **json.loads(args['params']))
