# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/modifier_widget.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from HWArenaPhasesComponent import HWArenaPhasesComponent as HWArenaPhasesComponent
from halloween.gui.scaleform.daapi.view.battle.fullscreen_watcher_mixin import FullscreenWatcherMixin as FullscreenWatcherMixin
from halloween.gui.scaleform.daapi.view.meta.PhaseModifierMeta import PhaseModifierMeta as PhaseModifierMeta
from typing import Optional as Optional
from gui.impl import backport as backport
from gui.impl.gen import R as R

class HWModifierWidget(FullscreenWatcherMixin, PhaseModifierMeta):
    ICONS_PATH = R.images.halloween.gui.maps.icons.battleHints
    BATTLE_HINT = R.strings.halloween_battle.battleHint
    needToShow: Any
    __modifierName: Any
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _update(self, arenaPhases):
        ...
    def _modifierChanged(self, modifierName):
        ...
