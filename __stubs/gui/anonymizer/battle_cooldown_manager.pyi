# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/anonymizer/battle_cooldown_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.shared.rq_cooldown import RequestCooldownManager as RequestCooldownManager, REQUEST_SCOPE as REQUEST_SCOPE
from messenger.proto.shared_errors import I18nActionID as I18nActionID

class BattleCooldownManager(RequestCooldownManager):
    __default: Any
    def __init__(self, default=1.0):
        ...
    def lookupName(self, rqTypeID):
        ...
    def getDefaultCoolDown(self):
        ...
