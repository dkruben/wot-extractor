# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/veh_post_progression/battle_cooldown_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.shared.rq_cooldown import RequestCooldownManager as RequestCooldownManager, REQUEST_SCOPE as REQUEST_SCOPE

class BattleCooldownManager(RequestCooldownManager):
    __default: Any
    def __init__(self, default=0.5):
        ...
    def lookupName(self, rqTypeID):
        ...
    def getDefaultCoolDown(self):
        ...
    def _showSysMessage(self, msg):
        ...
