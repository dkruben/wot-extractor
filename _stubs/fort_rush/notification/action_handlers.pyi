# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/notification/action_handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from fort_rush.gui.shared.event_dispatcher import showProgressionView as showProgressionView
from fort_rush.skeletons.battle_controller import IFortRushBattleController as IFortRushBattleController
from helpers import dependency as dependency
from notification.actions_handlers import NavigationDisabledActionHandler as NavigationDisabledActionHandler
from notification.settings import NOTIFICATION_TYPE as NOTIFICATION_TYPE

class FortRushActionHandler(NavigationDisabledActionHandler):
    _frCtrl: Any
    def doAction(self, model, entityID, action):
        ...
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def _canNavigate(self):
        ...

class _OpenFRProgressionHandler(FortRushActionHandler):
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def switchToFortRush(ctrl=None):
    ...
