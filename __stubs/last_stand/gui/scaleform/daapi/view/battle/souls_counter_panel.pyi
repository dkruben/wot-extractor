# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/souls_counter_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.shared.utils.graphics import isLowPreset as isLowPreset
from last_stand.gui.scaleform.daapi.view.meta.PointCounterMeta import PointCounterMeta as PointCounterMeta
from last_stand.gui.ls_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID

class LSSoulsCounter(PointCounterMeta):
    __sessionProvider: Any
    prevSoulsCount: Any
    capacity: Any
    _soulsContainer: Any
    def __init__(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _onSoulsContainerReady(self, vehicleSoulsContainer):
        ...
    def __onSoulsChanged(self, newCount, reason):
        ...
    def __enableAnimation(self):
        ...
