# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/scaleform/daapi/view/battle/shared/fort_rush_ingame_menu.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.Scaleform.daapi.view.battle.shared.ingame_menu import IngameMenu as IngameMenu
from gui.Scaleform.daapi.view.battle.shared.premature_leave import showResDialogWindow as showResDialogWindow
from gui.battle_control.battle_session import BattleExitResult as BattleExitResult
import BattleReplay as BattleReplay
from wg_async import wg_await as wg_await, wg_async as wg_async
from BWUtil import AsyncReturn as AsyncReturn
from gui.impl.gen import R as R

class FortRushIngameMenu(IngameMenu):
    def _getExitResult(self):
        ...
    @staticmethod
    def _showLeaverAliveWindow(isPlayerIGR):
        ...

# decorador original: @wg_async
def _showLeaverAliveWindow(quitR):
    ...
