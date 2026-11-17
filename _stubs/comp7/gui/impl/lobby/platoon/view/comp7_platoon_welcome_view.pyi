# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/platoon/view/comp7_platoon_welcome_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from comp7.gui.comp7_constants import SELECTOR_BATTLE_TYPES as SELECTOR_BATTLE_TYPES
from comp7.gui.prb_control.entities import comp7_prb_helpers as comp7_prb_helpers
from constants import QUEUE_TYPE as QUEUE_TYPE
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.platoon.platoon_helpers import getPlatoonBonusState as getPlatoonBonusState
from gui.impl.lobby.platoon.view.platoon_welcome_view import WelcomeView as WelcomeView
from gui.impl.lobby.premacc.squad_bonus_tooltip_content import SquadBonusTooltipContent as SquadBonusTooltipContent
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7Controller as IComp7Controller, IPlatoonController as IPlatoonController
_logger: Any
strButtons = R.strings.platoon.buttons

class Comp7WelcomeView(WelcomeView):
    __comp7Ctrl: Any
    __platoonCtrl: Any
    def __init__(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _initButtons(self):
        ...
    def _addListeners(self):
        ...
    def _removeListeners(self):
        ...
    def _setBattleTypeRelatedProps(self):
        ...
    def __onCreateForTwo(self):
        ...
    def __onCreateForSeven(self):
        ...
