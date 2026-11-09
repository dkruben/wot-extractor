# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/gui/battle_control/controllers/appearance_cache_ctrls/comp7_appearance_cache_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from future.utils import viewitems as viewitems
from gui.battle_control.controllers.appearance_cache_ctrls.default_appearance_cache_ctrl import DefaultAppearanceCacheController as DefaultAppearanceCacheController
_logger: Any

class Comp7AppearanceCacheController(DefaultAppearanceCacheController):
    __pendingReloads: Any
    def __init__(self, setup):
        ...
    def stopControl(self):
        ...
    def arenaLoadCompleted(self):
        ...
    def reloadAppearance(self, vId, vInfo, callback=None, strCD=None, oldStrCD=None):
        ...
