# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/seasons_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from constants import GameSeasonType as GameSeasonType
from soft_exception import SoftException as SoftException
from helpers import dependency as dependency
from skeletons.gui.game_control import ISeasonsController as ISeasonsController, IRankedBattlesController as IRankedBattlesController, IEpicBattleMetaGameController as IEpicBattleMetaGameController, IMapboxController as IMapboxController, IEventBattlesController as IEventBattlesController
from gui.shared.system_factory import registerSeasonProviderHandler as registerSeasonProviderHandler, collectSeasonProviderHandler as collectSeasonProviderHandler

class SeasonsController(ISeasonsController):
    def hasAnySeason(self, seasonType):
        ...
    def getCurrentSeason(self, seasonType):
        ...
    def getCurrentCycleID(self, seasonType):
        ...
    def getSeason(self, seasonType, seasonID):
        ...
    def isSeasonActive(self, seasonID, seasonType):
        ...
    def isWithinSeasonTime(self, seasonID, seasonType):
        ...
    def isSeasonCycleActive(self, cycleID, seasonType):
        ...
    def __getSeasonProviderChecked(self, seasonType):
        ...
