# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/battle_results/missions_progress/research.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from helpers import dependency as dependency
from comp7.gui.shared.gui_items.dossier.stats import getComp7DossierStats as getComp7DossierStats
from gui.battle_results.progress.research import VehicleProgressHelper as VehicleProgressHelper
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from comp7.gui.shared.gui_items.dossier.stats import AccountComp7StatsBlock as AccountComp7StatsBlock

class Comp7VehicleProgressHelper(VehicleProgressHelper):
    __comp7Ctrl: Any
    def _getAvgVehicleXp(self, vehTypeCompDescr):
        ...
