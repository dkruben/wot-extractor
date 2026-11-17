# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/base/actions_validator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import logging as logging
import weakref as weakref
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle, g_currentVehicle as g_currentVehicle
from gui.lobby_state_machine.states import LobbyStateFlags as LobbyStateFlags
from gui.prb_control.items import ValidationResult as ValidationResult
from gui.prb_control.settings import PREBATTLE_RESTRICTION as PREBATTLE_RESTRICTION
from helpers import dependency as dependency
from skeletons.tutorial import ITutorialLoader as ITutorialLoader
from soft_exception import SoftException as SoftException
from typing import Optional as Optional
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
_logger: Any

class IActionsValidator(object):
    def canPlayerDoAction(self):
        ...

class NotSupportedActionsValidator(IActionsValidator):
    def canPlayerDoAction(self):
        ...

class BaseActionsValidator(IActionsValidator):
    _entity: Any
    def __init__(self, entity):
        ...
    def canPlayerDoAction(self, ignoreEnable=False):
        ...
    def _validate(self):
        ...
    def _isEnabled(self):
        ...

class CurrentPreviewVehicleActionsValidator(BaseActionsValidator):
    def _validate(self):
        ...

class VehicleActionsValidator(object):
    @classmethod
    def validateVehicle(cls, vehicle):
        ...
    @classmethod
    def validateVehicleBool(cls, vehicle):
        ...

class CurrentVehicleActionsValidator(BaseActionsValidator):
    def _validate(self):
        ...

class TutorialActionsValidator(BaseActionsValidator):
    __tutorialLoader: Any
    def _validate(self):
        ...

class ActionsValidatorComposite(BaseActionsValidator):
    __validators: Any
    __warnings: Any
    def __init__(self, entity, validators=None, warnings=None):
        ...
    def addValidator(self, validator):
        ...
    def removeValidator(self, validator):
        ...
    def addWarning(self, warning):
        ...
    def removeWarning(self, warning):
        ...
    def _validate(self):
        ...
