# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/prb_control/entities/tournament/legacy/entity.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from helpers import dependency as dependency
from gui.prb_control import prb_getters as prb_getters
from gui.prb_control.settings import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG
from gui.prb_control.entities.base.legacy.entity import LegacyEntryPoint as LegacyEntryPoint
from skeletons.gui.game_control import IBattleRoyaleTournamentController as IBattleRoyaleTournamentController
from gui.prb_control.items import prb_seqs as prb_seqs

class BattleRoyaleTournamentEntryPoint(LegacyEntryPoint):
    __battleRoyaleTournamentController: Any
    def __init__(self):
        ...
    def join(self, ctx, callback=None):
        ...
