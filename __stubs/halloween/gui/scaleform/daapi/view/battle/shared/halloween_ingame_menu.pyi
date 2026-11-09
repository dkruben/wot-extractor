# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/shared/halloween_ingame_menu.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from BWUtil import AsyncReturn as AsyncReturn
import BattleReplay as BattleReplay
from wg_async import wg_async as wg_async, wg_await as wg_await
from gui.impl.gen import R as R
from HWArenaPhasesComponent import HWArenaPhasesComponent as HWArenaPhasesComponent
from gui.Scaleform.daapi.view.battle.shared.ingame_menu import IngameMenu as IngameMenu
from gui.Scaleform.daapi.view.battle.shared.premature_leave import showResDialogWindow as showResDialogWindow, showLeaverReplayWindow as showLeaverReplayWindow
from gui.Scaleform.daapi.view.battle.shared.premature_leave import showExitWindow as showExitWindow
from halloween.gui.impl.battle.help_view import HelpWindow as HelpWindow

class HWIngameMenu(IngameMenu):
    @property
    def arenaPhases(self):
        ...
    def helpClick(self):
        ...
    # decorador original: @wg_async
    def _doLeaveArena(self):
        ...
    def _isEventPrematureLeave(self):
        ...

# decorador original: @wg_async
def showLeaverAliveWindow():
    ...
