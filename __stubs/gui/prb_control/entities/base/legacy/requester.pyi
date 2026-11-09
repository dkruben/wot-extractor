# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/base/legacy/requester.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from PlayerEvents import g_playerEvents as g_playerEvents
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.prb_control.entities.base.requester import IPrbListRequester as IPrbListRequester
from gui.prb_control.items.prb_seqs import RosterIterator as RosterIterator

class LegacyRosterRequester(IPrbListRequester):
    __callback: Any
    __prebattleID: Any
    __ctx: Any
    def __init__(self):
        ...
    def start(self, callback):
        ...
    def stop(self):
        ...
    def request(self, ctx=None):
        ...
    def __pe_onPrebattleRosterReceived(self, prebattleID, roster):
        ...
