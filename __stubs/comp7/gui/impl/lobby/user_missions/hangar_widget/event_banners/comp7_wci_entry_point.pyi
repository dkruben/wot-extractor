# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/user_missions/hangar_widget/event_banners/comp7_wci_entry_point.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from comp7.gui.Scaleform.genConsts.COMP7_HANGAR_ALIASES import COMP7_HANGAR_ALIASES as COMP7_HANGAR_ALIASES
from comp7.gui.comp7_constants import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG
from comp7.gui.impl.lobby.user_missions.hangar_widget.event_banners.comp7_tournament_event_banner import Comp7TournamentEventBanner as Comp7TournamentEventBanner
from comp7.gui.shared import event_dispatcher as comp7_events
from helpers.ingame_tournament_helper import IngameTournamentType as IngameTournamentType
from skeletons.gui.game_control import IComp7Controller as IComp7Controller

class Comp7WCIEntryPoint(Comp7TournamentEventBanner):
    NAME = COMP7_HANGAR_ALIASES.COMP7_WCI_ENTRY_POINT
    _TOURNAMENT_TYPE = IngameTournamentType.WCI
    def onClick(self):
        ...
    @classmethod
    def isTournamentEntryPointAvailable(cls, comp7Ctrl=None):
        ...
    @classmethod
    def __isRandomPrbActive(cls):
        ...
