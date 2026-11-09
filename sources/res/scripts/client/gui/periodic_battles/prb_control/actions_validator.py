# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/periodic_battles/prb_control/actions_validator.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/periodic_battles/prb_control/actions_validator.py
from gui.prb_control.entities.base.actions_validator import BaseActionsValidator
from gui.prb_control.entities.base.unit.actions_validator import UnitStateValidator
from gui.prb_control.items import ValidationResult
from gui.prb_control.settings import PRE_QUEUE_RESTRICTION, UNIT_RESTRICTION
from gui.periodic_battles.models import PrimeTimeStatus

def _validateModeState(controller, restrictions):
    if controller is None:
        return ValidationResult(False, restrictions.UNDEFINED, None)
    else:
        if not controller.isBattlesPossible():
            return ValidationResult(False, restrictions.MODE_NO_BATTLES, None)
        status, _, _ = controller.getPrimeTimeStatus()
        if status == PrimeTimeStatus.NOT_SET:
            return ValidationResult(False, restrictions.MODE_NOT_SET, None)
        if status != PrimeTimeStatus.AVAILABLE:
            return ValidationResult(False, restrictions.MODE_NOT_AVAILABLE, None)
        return


class PrimeTimeValidator(BaseActionsValidator):

    def _getController(self):
        raise NotImplementedError

    def _validate(self):
        validationRes = _validateModeState(self._getController(), PRE_QUEUE_RESTRICTION)
        if validationRes is not None:
            return validationRes
        else:
            return super(PrimeTimeValidator, self)._validate()


class SquadPrimeTimeValidator(UnitStateValidator):

    def _getController(self):
        raise NotImplementedError

    def _validate(self):
        validationRes = _validateModeState(self._getController(), UNIT_RESTRICTION)
        if validationRes is not None:
            return validationRes
        else:
            return super(SquadPrimeTimeValidator, self)._validate()
