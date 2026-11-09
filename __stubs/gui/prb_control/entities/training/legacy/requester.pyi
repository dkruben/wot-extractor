# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/training/legacy/requester.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from PlayerEvents import g_playerEvents as g_playerEvents
from constants import PREBATTLE_TYPE as PREBATTLE_TYPE, PREBATTLE_CACHE_KEY as PREBATTLE_CACHE_KEY
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.prb_control.entities.base.requester import IPrbListRequester as IPrbListRequester
from gui.prb_control.items import prb_seqs as prb_seqs

class TrainingListRequester(IPrbListRequester):
    UPDATE_LIST_TIMEOUT = 5
    __callbackID: Any
    __callback: Any
    def __init__(self):
        ...
    def start(self, callback):
        ...
    def stop(self):
        ...
    def request(self, ctx=None):
        ...
    def __request(self):
        ...
    def __setTimeout(self):
        ...
    def __pe_onPrebattlesListReceived(self, prbType, count, prebattles):
        ...
