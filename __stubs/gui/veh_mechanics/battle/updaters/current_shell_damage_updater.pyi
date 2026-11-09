# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/veh_mechanics/battle/updaters/current_shell_damage_updater.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import logging as logging
import typing as typing
from gui.veh_mechanics.battle.updaters.updaters_common import ViewUpdater as ViewUpdater
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from typing import Any as Any
from gui.battle_control.controllers.consumables.ammo_ctrl import AmmoController as AmmoController
_logger: _Any

class CurrentShellDamageUpdater(ViewUpdater):
    __sessionProvider: _Any
    __currentDamage: _Any
    def __init__(self, view):
        ...
    def initialize(self):
        ...
    def finalize(self):
        ...
    def __getCurrentShellDamage(self):
        ...
    def __onCurrentShellDamageChanged(self, *_):
        ...
