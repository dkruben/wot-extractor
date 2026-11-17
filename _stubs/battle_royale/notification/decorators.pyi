# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/notification/decorators.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from helpers import dependency as dependency
from notification.decorators import MessageDecorator as MessageDecorator
from notification.settings import NOTIFICATION_BUTTON_STATE as NOTIFICATION_BUTTON_STATE
from battle_royale.skeletons.game_controller import IBRProgressionOnTokensController as IBRProgressionOnTokensController

class BRProgressionLockButtonDecorator(MessageDecorator):
    _brProgressionController: Any
    def __init__(self, entityID, entity=None, settings=None, model=None):
        ...
    def clear(self):
        ...
    def _make(self, entity=None, settings=None):
        ...
    def __updateEntityButtons(self):
        ...
    def __update(self, *_):
        ...
