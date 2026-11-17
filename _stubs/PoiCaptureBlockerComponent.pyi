# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/PoiCaptureBlockerComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import CGF as CGF
from PoiBaseComponent import PoiBaseComponent as PoiBaseComponent
from helpers import fixed_dict as fixed_dict
from points_of_interest.components import PoiCaptureBlockerStateComponent as PoiCaptureBlockerStateComponent
from points_of_interest_shared import PoiBlockReasons as PoiBlockReasons
_logger: Any

class PoiCaptureBlockerComponent(PoiBaseComponent):
    def onDestroy(self):
        ...
    def set_blockReasons(self, prev):
        ...
    def _onAvatarReady(self):
        ...
    def __getBlockReasons(self):
        ...
