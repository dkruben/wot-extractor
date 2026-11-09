# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/prb_control/entities/tournament/pre_queue/action_validator.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/prb_control/entities/tournament/pre_queue/action_validator.py
from __future__ import absolute_import
from gui.prb_control.entities.base.actions_validator import ActionsValidatorComposite
from gui.prb_control.entities.base.pre_queue.actions_validator import PreQueueActionsValidator, InQueueValidator
from gui.prb_control.items import ValidationResult

class _BattleRoyaleTournamentInQueueValidator(InQueueValidator):

    def _validate(self):
        if self._entity.isInQueue():
            return ValidationResult(True)
        return super(_BattleRoyaleTournamentInQueueValidator, self)._validate()


class BattleRoyaleTournamentActionsValidator(PreQueueActionsValidator):

    def _createStateValidator(self, entity):
        return ActionsValidatorComposite(entity, [
         _BattleRoyaleTournamentInQueueValidator(entity)])
