# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/frontline_full_stats.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from frontline.gui.Scaleform.daapi.view.meta.FrontlineFullStatsMeta import FrontlineFullStatsMeta as FrontlineFullStatsMeta
from gui.Scaleform.locale.EPIC_BATTLE import EPIC_BATTLE as EPIC_BATTLE
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from helpers import i18n as i18n

class FrontlineFullStatsComponent(FrontlineFullStatsMeta):
    sessionProvider: Any
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __setGeneralBonus(self, newFactor, allyVehID=None, allyNewRank=None):
        ...
