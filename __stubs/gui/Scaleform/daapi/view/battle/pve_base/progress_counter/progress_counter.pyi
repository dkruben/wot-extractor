# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/pve_base/progress_counter/progress_counter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import BattleReplay as BattleReplay
from gui.Scaleform.daapi.view.battle.pve_base.base.pve_hud_widget import SingleItemPveHudWidget as SingleItemPveHudWidget
from gui.Scaleform.daapi.view.battle.pve_base.progress_counter.settings_model import ProgressCounterServerModel as ProgressCounterServerModel
from gui.Scaleform.daapi.view.battle.pve_base.progress_counter.state_machine.machine import ProgressCounterStateMachine as ProgressCounterStateMachine
from gui.Scaleform.daapi.view.meta.PveProgressCounterMeta import PveProgressCounterMeta as PveProgressCounterMeta
from pve_battle_hud import WidgetType as WidgetType, ProgressCounterState as ProgressCounterState

class PveProgressCounter(SingleItemPveHudWidget, PveProgressCounterMeta):
    def __init__(self):
        ...
    def _getStateToRestore(self, serverSettings):
        ...
    def _onPrebattlePeriod(self):
        ...
