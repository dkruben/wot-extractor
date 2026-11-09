# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/uilogging/last_stand/loggers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/uilogging/last_stand/loggers.py
from __future__ import absolute_import
from typing import TYPE_CHECKING
from last_stand.uilogging.last_stand.constants import NarrationLogAction, FEATURE
from uilogging.base.logger import MetricsLogger
if TYPE_CHECKING:
    from uilogging.types import ItemType

class NarrationEventLogger(MetricsLogger):
    __slots__ = ()

    def __init__(self):
        super(NarrationEventLogger, self).__init__(FEATURE)

    def logStartEvent(self, item):
        self.log(NarrationLogAction.START, item)

    def logEndEvent(self, item):
        self.log(NarrationLogAction.END, item)
