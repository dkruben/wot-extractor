# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/pet_system/processor.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
from gui.impl import backport as backport
from gui import SystemMessages as SystemMessages
from gui.impl.gen import R as R
from gui.shared.gui_items.processors import Processor as Processor
_logger: Any

class PetSystemProcessor(Processor):
    def _errorHandler(self, code, errStr='', ctx=None):
        ...

class PetEventOpenProcessor(PetSystemProcessor):
    def _request(self, callback):
        ...

class SelectActivePetProcessor(PetSystemProcessor):
    __petID: Any
    def __init__(self, petID):
        ...
    def _request(self, callback):
        ...

class SelectPetNameProcessor(PetSystemProcessor):
    __petID: Any
    __petNameID: Any
    def __init__(self, petID, petNameID):
        ...
    def _request(self, callback):
        ...

class SelectPetStateProcessor(PetSystemProcessor):
    __visibilityState: Any
    def __init__(self, visibilityState):
        ...
    def _request(self, callback):
        ...

class SelectPetActiveBonusProcessor(PetSystemProcessor):
    __bonusID: Any
    def __init__(self, bonusID):
        ...
    def _request(self, callback):
        ...

class FirstClickSynergyProcessor(PetSystemProcessor):
    __petID: Any
    def __init__(self, petID):
        ...
    def _request(self, callback):
        ...

class PetPurchaseProcessor(PetSystemProcessor):
    __petID: Any
    def __init__(self, petID):
        ...
    def _request(self, callback):
        ...
