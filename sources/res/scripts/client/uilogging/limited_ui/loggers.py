# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/uilogging/limited_ui/loggers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/limited_ui/loggers.py
from __future__ import absolute_import
import typing
from uilogging.base.logger import MetricsLogger
from uilogging.limited_ui.constants import FEATURE, LimitedUILogActions
if typing.TYPE_CHECKING:
    from uilogging.types import ItemType, ParentScreenType

class LimitedUILogger(MetricsLogger):
    __slots__ = ()

    def __init__(self):
        super(LimitedUILogger, self).__init__(FEATURE)

    def handleClickOnce(self, item, parentScreen):
        self.logOnce(action=LimitedUILogActions.CLICK, item=item, parentScreen=parentScreen)
