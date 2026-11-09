# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/base/legacy/actions_validator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from PlayerEvents import g_playerEvents as g_playerEvents
from gui.prb_control.entities.base.actions_validator import BaseActionsValidator as BaseActionsValidator, ActionsValidatorComposite as ActionsValidatorComposite
from gui.prb_control.items import ValidationResult as ValidationResult
from gui.prb_control.settings import PREBATTLE_RESTRICTION as PREBATTLE_RESTRICTION, PREBATTLE_SETTING_NAME as PREBATTLE_SETTING_NAME
from prebattle_shared import decodeRoster as decodeRoster
from typing import Dict as Dict, List as List, Type as Type
from constants import ARENA_GUI_TYPE as ARENA_GUI_TYPE
ARENA_GUI_TYPE_VALIDATORS: dict

class InQueueValidator(BaseActionsValidator):
    def _validate(self):
        ...

class LegacyVehicleValid(BaseActionsValidator):
    def _validate(self):
        ...

class LegacyTeamValidator(BaseActionsValidator):
    def _validate(self):
        ...
    def _isEnabled(self):
        ...

class LegacyActionsValidator(ActionsValidatorComposite):
    def __init__(self, entity):
        ...
