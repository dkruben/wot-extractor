# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/personal_reserves/personal_reserves_intro.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import typing as typing
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity as EventSystemEntity
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.personal_reserves.reserves_intro_view_model import ReservesIntroViewModel as ReservesIntroViewModel
from gui.impl.lobby.personal_reserves.reserves_constants import PERSONAL_RESERVES_SOUND_SPACE as PERSONAL_RESERVES_SOUND_SPACE
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow as LobbyWindow
from gui.shared.event_dispatcher import showPersonalReservesInfomationScreen as showPersonalReservesInfomationScreen
from helpers import dependency as dependency
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from typing import Dict as Dict, Any as Any

class PersonalReservesIntro(ViewImpl, EventSystemEntity):
    __slots__: tuple
    _COMMON_SOUND_SPACE = PERSONAL_RESERVES_SOUND_SPACE
    _uiLoader: _Any
    def __init__(self, layoutID, ctx=None):
        ...
    @property
    def viewModel(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def close(self):
        ...
    def _onDetailsClicked(self):
        ...

class PersonalReservesIntroWindow(LobbyWindow):
    __slots__: tuple
    def __init__(self, ctx=None):
        ...
