# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/vse_hud_settings_ctrl/settings/primary_objective.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from typing import List as List
from gui.battle_control.controllers.vse_hud_settings_ctrl.settings.base_models import TextClientModel as TextClientModel

class PrimaryObjectiveClientModel(TextClientModel):
    __slots__: tuple
    id: Any
    header: Any
    subheader: Any
    startSound: Any
    remindTimers: Any
    remindSound: Any
    countdownTimer: Any
    countdownSound: Any
    success: Any
    successIcon: Any
    successSound: Any
    failure: Any
    failureIcon: Any
    failureSound: Any
    def __init__(self, id, header, subheader, startSound, remindTimers, remindSound, countdownTimer, countdownSound, success, successIcon, successSound, failure, failureIcon, failureSound):
        ...
    def getHeader(self):
        ...
    def getSubheader(self, params):
        ...
    def getSuccess(self):
        ...
    def getFailure(self):
        ...
    def __repr__(self):
        ...
