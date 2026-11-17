# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/Scaleform/daapi/view/lobby/header/helpers/controls_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from comp7_light.gui.Scaleform.daapi.view.lobby.header.helpers.fight_btn_tooltips import getComp7LightFightBtnTooltipData as getComp7LightFightBtnTooltipData
from comp7_light.gui.impl.lobby.page.lobby_footer import Comp7LightLobbyFooter as Comp7LightLobbyFooter
from comp7_light.gui.impl.lobby.page.lobby_header import Comp7LightLobbyHeader as Comp7LightLobbyHeader
from gui.Scaleform.daapi.view.lobby.header.helpers.controls_helpers import DefaultLobbyHeaderHelper as DefaultLobbyHeaderHelper
from gui.impl.gen import R as R
from helpers import dependency as dependency, int2roman as int2roman
from skeletons.gui.game_control import IComp7LightController as IComp7LightController, IPlatoonController as IPlatoonController
from gui.prb_control.items import ValidationResult as ValidationResult
from gui.impl.pub.view_component import ViewComponent as ViewComponent

class Comp7LightLobbyHeaderHelper(DefaultLobbyHeaderHelper):
    __slots__: tuple
    __comp7LightController: Any
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
