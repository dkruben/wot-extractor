# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/hint_panel/plugins.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CommandMapping as CommandMapping
from gui.impl import backport as backport
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.Scaleform.daapi.view.battle.shared.hint_panel.hint_panel_plugin import HintPriority as HintPriority, HintData as HintData
from gui.Scaleform.daapi.view.battle.shared.hint_panel.plugins import PreBattleHintPlugin as PreBattleHintPlugin
from gui.impl.gen import R as R
from gui.shared.utils.key_mapping import getReadableKey as getReadableKey, getVirtualKey as getVirtualKey
from halloween_common.halloween_constants import ARENA_GUI_TYPE as ARENA_GUI_TYPE

class HWHelpPlugin(PreBattleHintPlugin):
    __sessionProvider: Any
    @classmethod
    def isSuitable(cls):
        ...
    def _getHint(self):
        ...
    def _canDisplayCustomHelpHint(self):
        ...

def updatePlugins(plugins):
    ...
