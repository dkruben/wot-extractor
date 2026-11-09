# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/prb_control/entities/squad/actions_validator.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/prb_control/entities/squad/actions_validator.py
from __future__ import absolute_import
import typing
from fort_rush.skeletons.battle_controller import IFortRushBattleController
from gui.prb_control.entities.base.actions_validator import ActionsValidatorComposite
from gui.prb_control.entities.base.squad.actions_validator import SquadActionsValidator, SquadVehiclesValidator
from gui.prb_control.entities.random.squad.actions_validator import SquadRestrictionsVehiclesValidator
from gui.prb_control.items import ValidationResult
from gui.prb_control.settings import UNIT_RESTRICTION
from helpers import dependency
if typing.TYPE_CHECKING:
    from gui.prb_control.entities.base.entity import BasePrbEntity
    from Vehicle import Vehicle

class FortRushSquadVehiclesValidator(SquadVehiclesValidator):
    battleController = dependency.descriptor(IFortRushBattleController)

    def _isVehicleSuitableForMode(self, vehicle):
        if not self._isValidMode(vehicle):
            return ValidationResult(False, UNIT_RESTRICTION.UNSUITABLE_VEHICLE)
        else:
            return

    def _isValidMode(self, vehicle):
        return self.battleController.isSuitableVehicle(vehicle) is None


class FortRushSquadActionsValidator(SquadActionsValidator):

    def _createVehiclesValidator(self, entity):
        return ActionsValidatorComposite(entity, validators=[
         FortRushSquadVehiclesValidator(entity),
         SquadRestrictionsVehiclesValidator(entity)])
