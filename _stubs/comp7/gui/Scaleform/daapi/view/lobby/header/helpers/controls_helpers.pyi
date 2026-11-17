# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/Scaleform/daapi/view/lobby/header/helpers/controls_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from comp7.gui.Scaleform.daapi.view.lobby.header.helpers.fight_btn_tooltips import getComp7FightBtnTooltipData as getComp7FightBtnTooltipData
from comp7.gui.impl.lobby.page.lobby_footer import Comp7LobbyFooter as Comp7LobbyFooter
from comp7.gui.impl.lobby.page.lobby_header import Comp7LobbyHeader as Comp7LobbyHeader
from gui.Scaleform.daapi.view.lobby.header.helpers.controls_helpers import DefaultLobbyHeaderHelper as DefaultLobbyHeaderHelper
from gui.impl.gen import R as R
from gui.prb_control.settings import PRE_QUEUE_RESTRICTION as PRE_QUEUE_RESTRICTION
from helpers import dependency as dependency, int2roman as int2roman
from skeletons.gui.game_control import IComp7Controller as IComp7Controller, IPlatoonController as IPlatoonController
from gui.prb_control.items import ValidationResult as ValidationResult
from gui.impl.pub.view_component import ViewComponent as ViewComponent

class Comp7LobbyHeaderHelper(DefaultLobbyHeaderHelper):
    __slots__: tuple
    __comp7Controller: Any
    __platoonController: Any
    @classmethod
    def _getDisabledFightTooltipData(cls, prbValidation, isInSquad):
        ...
    @classmethod
    def _getOutSquadTooltipData(cls, prbValidation):
        ...
    @classmethod
    def getHeaderType(cls):
        ...
    @classmethod
    def getFooterType(cls):
        ...
