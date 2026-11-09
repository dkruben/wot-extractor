# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/rankedBattles/ranked_battles_qualification.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import IS_FIRST_ENTRY_BY_DIVISION_ID as IS_FIRST_ENTRY_BY_DIVISION_ID
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.daapi.view.meta.RankedBattlesDivisionQualificationMeta import RankedBattlesDivisionQualificationMeta as RankedBattlesDivisionQualificationMeta
from gui.Scaleform.genConsts.RANKEDBATTLES_ALIASES import RANKEDBATTLES_ALIASES as RANKEDBATTLES_ALIASES
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.ranked_battles import ranked_formatters as ranked_formatters
from gui.ranked_battles.ranked_builders import shared_vos as shared_vos
from gui.shared.formatters import text_styles as text_styles, icons as icons
from helpers import dependency as dependency
from shared_utils import findFirst as findFirst
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController

class RankedBattlesQualification(RankedBattlesDivisionQualificationMeta):
    __rankedController: Any
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __updateRankedData(self, rank):
        ...
    def __dossierUpdateCallBack(self, *args):
        ...
    def __onRankedUpdate(self, *args):
        ...
    def __setQualificationData(self, rank):
        ...
    def __getQualificationRank(self):
        ...
    def __setQualificationProgress(self, rank):
        ...
    def __setQualificationSteps(self, divisionID):
        ...
    def __setQualificationEfficiency(self, divisionsID):
        ...
