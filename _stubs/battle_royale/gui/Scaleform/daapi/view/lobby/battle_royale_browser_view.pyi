# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/lobby/battle_royale_browser_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.lobby.shared.web_view import WebView as WebView
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController
from web.web_client_api.battle_royale import createBattleRoyaleWebHanlders as createBattleRoyaleWebHanlders

class BattleRoyaleBrowserView(WebView):
    __battleRoyaleController: Any
    def webHandlers(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __onSettingsChange(self, diff):
        ...
