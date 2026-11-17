# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/shared/gui_items/processors/plugins.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.shared.gui_items.processors.plugins import SyncValidator as SyncValidator, makeError as makeError, makeSuccess as makeSuccess

class CheckArtefact(SyncValidator):
    controller: Any
    artefactID: Any
    isSkipQuest: Any
    def __init__(self, controller, artefactID, isSkipQuest, isEnabled=True):
        ...
    def _validate(self):
        ...

class CheckTwitchCon(SyncValidator):
    controller: Any
    commanderIDs: Any
    def __init__(self, controller, commanderIDs, isEnabled=True):
        ...
    def _validate(self):
        ...
