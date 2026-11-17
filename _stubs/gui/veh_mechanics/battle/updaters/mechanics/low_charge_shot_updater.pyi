# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/veh_mechanics/battle/updaters/mechanics/low_charge_shot_updater.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.veh_mechanics.battle.updaters.updaters_common import ViewUpdater as ViewUpdater
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class LowChargeShotUpdater(ViewUpdater):
    __sessionProvider: Any
    def initialize(self):
        ...
    def finalize(self):
        ...
    def __onShellChangeTimeUpdated(self, isVisible, shellChangeTimes):
        ...
    def __onGunReloadTimeSet(self, _, state, __):
        ...
