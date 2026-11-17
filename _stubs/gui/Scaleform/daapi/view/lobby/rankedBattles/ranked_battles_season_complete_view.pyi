# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/rankedBattles/ranked_battles_season_complete_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from future.utils import viewitems as viewitems
import SoundGroups as SoundGroups
from gui.Scaleform.daapi.view.meta.RankedBattlesSeasonCompleteViewMeta import RankedBattlesSeasonCompleteViewMeta as RankedBattlesSeasonCompleteViewMeta
from gui.impl import backport as backport
from gui.ranked_battles import ranked_helpers as ranked_helpers
from gui.ranked_battles.constants import RankedDossierKeys as RankedDossierKeys
from gui.ranked_battles.ranked_builders import season_comple_vos as season_comple_vos
from gui.ranked_battles.ranked_formatters import getRankedAwardsFormatter as getRankedAwardsFormatter
from gui.ranked_battles.ranked_helpers.web_season_provider import UNDEFINED_LEAGUE_ID as UNDEFINED_LEAGUE_ID
from gui.server_events.awards_formatters import AWARDS_SIZES as AWARDS_SIZES
from gui.server_events.bonuses import getBonuses as getBonuses
from gui.Scaleform.genConsts.RANKEDBATTLES_CONSTS import RANKEDBATTLES_CONSTS as RANKEDBATTLES_CONSTS
from helpers import dependency as dependency
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any

class RankedBattlesSeasonCompleteView(RankedBattlesSeasonCompleteViewMeta):
    __rankedController: Any
    __itemsCache: Any
    _quest: Any
    _awards: Any
    def __init__(self, ctx=None):
        ...
    def closeView(self):
        ...
    def onSoundTrigger(self, soundName):
        ...
    def showRating(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __getPosition(self):
        ...
    def __packAwards(self):
        ...
    def __setData(self):
        ...
    def __updatePosition(self):
        ...
