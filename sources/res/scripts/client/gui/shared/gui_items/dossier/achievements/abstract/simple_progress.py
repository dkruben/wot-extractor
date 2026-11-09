# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/gui_items/dossier/achievements/abstract/simple_progress.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/abstract/simple_progress.py
from __future__ import absolute_import, division
from gui.shared.gui_items.dossier.achievements.abstract.regular import RegularAchievement
from dossiers2.custom.config import RECORD_CONFIGS

class SimpleProgressAchievement(RegularAchievement):
    __slots__ = ('_progressValue', )

    def __init__(self, name, block, dossier, value=None):
        if dossier is not None:
            self._progressValue = self._readProgressValue(dossier)
        else:
            self._progressValue = 0
        super(SimpleProgressAchievement, self).__init__(name, block, dossier, value)
        return

    def getProgressValue(self):
        if not self._lvlUpTotalValue:
            return 1.0
        return 1 - float(self._lvlUpValue) / float(self._lvlUpTotalValue)

    def isInNear(self):
        return self.getProgressValue() > 0

    def hasProgress(self):
        return not self._isDone

    def _readLevelUpValue(self, dossier):
        minValue = RECORD_CONFIGS[self._name]
        _, series = divmod(self._progressValue, minValue)
        return minValue - series

    def _readLevelUpTotalValue(self, dossier):
        return RECORD_CONFIGS[self._name]

    def _readProgressValue(self, dossier):
        return 0
