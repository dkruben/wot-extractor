# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_control/controllers/battle_hints/component.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/battle_hints/component.py
from __future__ import absolute_import
import typing
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from gui.battle_control.controllers.battle_hints.common import getLogger
from gui.battle_control.controllers.battle_hints.queues import BattleHintQueueParams
if typing.TYPE_CHECKING:
    from hints.battle.schemas.base import CHMType
    from gui.battle_control.controllers.battle_hints.controller import BattleHintsController
_logger = getLogger('Component')

class IBattleHintView(object):

    def showHint(self, model, params):
        pass

    def hideHint(self, hint=None):
        pass


class BattleHintComponent(IBattleHintView):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self, battleHintsQueueParams=None, *args, **kwargs):
        self.__battleHintsQueueParams = battleHintsQueueParams
        if self.__battleHintsQueueParams is None:
            self.__battleHintsQueueParams = BattleHintQueueParams(name=('{}_{}').format(self.__class__.__name__, id(self)))
        super(BattleHintComponent, self).__init__(*args, **kwargs)
        _logger.debug('Initialized with queue params %s.', self.__battleHintsQueueParams)
        return

    def getBattleHintsQueueParams(self):
        return self.__battleHintsQueueParams

    def showHint(self, model, params=None):
        self._showHint(model, params)

    def hideHint(self):
        self._hideHint()

    def cancelFadeOut(self):
        self._cancelFadeOut()

    def onFadeOutFinished(self):
        battleHints = self.__sessionProvider.dynamic.battleHints
        if not battleHints:
            _logger.warning('No battle hint controller on fade out finished event.')
            return
        battleHints.onFadeOutFinished(self)

    def _showHint(self, model, params):
        raise NotImplementedError

    def _hideHint(self):
        raise NotImplementedError

    def _cancelFadeOut(self):
        pass
