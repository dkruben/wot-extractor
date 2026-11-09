# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/prb_control/entities/pre_queue/actions_validator.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/prb_control/entities/pre_queue/actions_validator.py
from __future__ import absolute_import
from CurrentVehicle import g_currentVehicle
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasDesiredSubMode
from gui.prb_control.entities.base.actions_validator import ActionsValidatorComposite
from gui.prb_control.entities.base.pre_queue.actions_validator import PreQueueActionsValidator
from gui.periodic_battles.prb_control.actions_validator import PrimeTimeValidator, BaseActionsValidator

class FunRandomPrimeTimeValidator(PrimeTimeValidator, FunSubModesWatcher):

    def _getController(self):
        return self.getDesiredSubMode()


class FunRandomVehicleValidator(BaseActionsValidator, FunSubModesWatcher):

    def _validate(self):
        validationResult = None
        if g_currentVehicle.isPresent():
            validationResult = self.__validate(g_currentVehicle.item)
        return validationResult or super(FunRandomVehicleValidator, self)._validate()

    @hasDesiredSubMode()
    def __validate(self, vehicle):
        return self.getDesiredSubMode().isSuitableVehicle(vehicle)


class FunRandomActionsValidator(PreQueueActionsValidator):

    def _createStateValidator(self, entity):
        baseValidator = super(FunRandomActionsValidator, self)._createStateValidator(entity)
        return ActionsValidatorComposite(entity, [baseValidator, FunRandomPrimeTimeValidator(entity)])

    def _createVehiclesValidator(self, entity):
        baseValidator = super(FunRandomActionsValidator, self)._createVehiclesValidator(entity)
        return ActionsValidatorComposite(entity, [FunRandomVehicleValidator(entity), baseValidator])
