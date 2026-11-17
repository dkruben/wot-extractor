# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/lobby/header/helpers/controls_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.impl.gen import R as R
from gui.Scaleform.daapi.view.lobby.header.helpers.controls_helpers import DefaultLobbyHeaderHelper as DefaultLobbyHeaderHelper
from last_stand.gui.scaleform.daapi.view.lobby.header.helpers.fight_btn_tooltips import getLSFightButtonTooltipData as getLSFightButtonTooltipData
from last_stand.gui.impl.lobby.page.ls_lobby_header import LSLobbyHeader as LSLobbyHeader
from last_stand.gui.impl.lobby.page.ls_lobby_footer import LSLobbyFooter as LSLobbyFooter
from gui.impl.pub.view_component import ViewComponent as ViewComponent

class LSLobbyHeaderHelper(DefaultLobbyHeaderHelper):
    __slots__: tuple
    @classmethod
    def getHeaderType(cls):
        ...
    @classmethod
    def getFooterType(cls):
        ...
    @classmethod
    def _getDisabledFightTooltipData(cls, prbValidation, isInSquad):
        ...
    @classmethod
    def _getOutSquadTooltipData(cls, _):
        ...
