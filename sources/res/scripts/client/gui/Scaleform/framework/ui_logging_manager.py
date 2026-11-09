# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/framework/ui_logging_manager.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/framework/ui_logging_manager.py
from __future__ import absolute_import
from gui.Scaleform.framework.entities.abstract.UILoggerManagerMeta import UILoggerManagerMeta
from gui.shared.utils import flashObject2Dict
from helpers import dependency
from skeletons.ui_logging import IUILoggingCore
from wotdecorators import noexcept

class UILoggerManager(UILoggerManagerMeta):
    _logger = dependency.descriptor(IUILoggingCore)

    @noexcept
    def onLog(self, feature, group, action, logLevel, params):
        self._logger.log(feature, group, action, logLevel, **flashObject2Dict(params))
