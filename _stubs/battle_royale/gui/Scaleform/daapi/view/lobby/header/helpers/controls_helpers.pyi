# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/lobby/header/helpers/controls_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.impl.gen import R as R
from gui.Scaleform.daapi.view.lobby.header.helpers.controls_helpers import DefaultLobbyHeaderHelper as DefaultLobbyHeaderHelper
from gui.Scaleform.daapi.view.lobby.header.helpers.fight_btn_tooltips import getRoyaleFightBtnTooltipData as getRoyaleFightBtnTooltipData
from battle_royale.gui.Scaleform.daapi.view.lobby.footer.battle_royale_lobby_footer import BattleRoyaleLobbyFooter as BattleRoyaleLobbyFooter

class BattleRoyaleLobbyHeaderHelper(DefaultLobbyHeaderHelper):
    _IN_SQUAD_TOOLTIP_KEY = 'battleRoyaleSquad'
    _OUT_SQUAD_TOOLTIP_KEY = 'battleRoyaleSquad'
    @classmethod
    def _getDisabledFightTooltipData(cls, prbValidation, isInSquad):
        ...
    @classmethod
    def getFooterType(cls):
        ...

class BRTournamentLobbyHeaderHelper(DefaultLobbyHeaderHelper):
    __slots__: tuple
    @classmethod
    def getFightControlTooltipData(cls, prbValidation, isInSquad, isFightBtnDisabled, isNavigationEnabled):
        ...
    @classmethod
    def getSquadControlTooltipData(cls, prbValidation, isInSquad):
        ...
