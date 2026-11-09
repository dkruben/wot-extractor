# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/prb_control/entities/pre_queue/actions_validator.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/prb_control/entities/pre_queue/actions_validator.py
from __future__ import absolute_import
from gui.prb_control.settings import PRE_QUEUE_RESTRICTION
from helpers import dependency
from CurrentVehicle import g_currentVehicle
from gui.prb_control.entities.base.pre_queue.actions_validator import PreQueueActionsValidator
from gui.prb_control.items import ValidationResult
from gui.prb_control.entities.base.actions_validator import BaseActionsValidator, ActionsValidatorComposite
from halloween.skeletons.halloween_controller import IHalloweenController

class HalloweenStateValidator(BaseActionsValidator):
    __halloweenBattleCtrl = dependency.descriptor(IHalloweenController)

    def _validate(self):
        if not self.__halloweenBattleCtrl.isBattlesEnabled():
            return ValidationResult(False, PRE_QUEUE_RESTRICTION.MODE_NOT_AVAILABLE)
        vehicle = g_currentVehicle.item
        if vehicle and not self.__halloweenBattleCtrl.hasAccessToVehicle(vehicle.intCD):
            return ValidationResult(False, PRE_QUEUE_RESTRICTION.VEHICLE_WILL_BE_UNLOCKED)
        return super(HalloweenStateValidator, self)._validate()


class HalloweenVehicleValidator(BaseActionsValidator):

    def _validate(self):
        vehicle = g_currentVehicle.item
        if vehicle is None:
            return ValidationResult(False)
        else:
            return super(HalloweenVehicleValidator, self)._validate()


class HalloweenActionsValidator(PreQueueActionsValidator):

    def _createVehiclesValidator(self, entity):
        baseValidator = super(HalloweenActionsValidator, self)._createVehiclesValidator(entity)
        return ActionsValidatorComposite(entity, [
         HalloweenVehicleValidator(entity),
         HalloweenStateValidator(entity),
         baseValidator])
