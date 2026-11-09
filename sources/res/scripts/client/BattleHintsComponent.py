# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/BattleHintsComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/BattleHintsComponent.py
from __future__ import absolute_import
import typing, logging
from BigWorld import DynamicScriptComponent
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
_logger = logging.getLogger(__name__)
if typing.TYPE_CHECKING:
    from gui.battle_control.controllers.battle_hints.controller import BattleHintsController

class BattleHintsComponent(DynamicScriptComponent):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def showHint(self, hintName, hintParams, immediately=False):
        controller = self.sessionProvider.dynamic.battleHints
        if controller:
            controller.showHint(hintName=hintName, params=dict(hintParams), immediately=immediately)
        else:
            _logger.warning('No battle hints controller on show hint call.')

    def hideHint(self, hintName):
        controller = self.sessionProvider.dynamic.battleHints
        if controller:
            controller.hideHint(hintName=hintName)
        else:
            _logger.warning('No battle hints controller on hide hint call.')

    def removeHint(self, hintName, hide=False):
        controller = self.sessionProvider.dynamic.battleHints
        if controller:
            controller.removeHint(hintName=hintName, hide=hide)
        else:
            _logger.warning('No battle hints controller on remove hint call.')
