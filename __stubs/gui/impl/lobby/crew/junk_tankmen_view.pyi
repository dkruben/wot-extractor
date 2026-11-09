# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/junk_tankmen_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import nations as nations
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowLayer as WindowLayer, WindowFlags as WindowFlags
from gui.impl.gen.view_models.views.lobby.crew.junk_tankmen_view_model import JunkTankmenViewModel as JunkTankmenViewModel
from gui.impl.lobby.crew.base_tankman_list_view import BaseTankmanListView as BaseTankmanListView
from gui.impl.lobby.crew.filter.data_providers import JunkTankmenDataProvider as JunkTankmenDataProvider
from gui.impl.lobby.crew.crew_helpers.model_setters import setTankmanModel as setTankmanModel, setTmanSkillsModel as setTmanSkillsModel
from gui.impl.gen.view_models.views.lobby.crew.tankman_model import TankmanModel as TankmanModel
from gui.impl.gen import R as R
from gui.impl.pub import WindowImpl as WindowImpl
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.game_control import restore_contoller as restore_contoller
from PlayerEvents import g_playerEvents as g_playerEvents

class JunkTankmenView(BaseTankmanListView):
    itemsCache: Any
    __slots__: tuple
    __dataProvider: Any
    def __init__(self, layoutID=..., *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    @property
    def _tankmenProvider(self):
        ...
    @property
    def _recruitsProvider(self):
        ...
    @property
    def _filterState(self):
        ...
    def _fillTankmanCard(self, cardsList, tankman):
        ...
    def _fillRecruits(self, cardsList, limit, offset):
        ...
    def _onClose(self):
        ...
    def _onConfirm(self):
        ...
    def _fillRecruitCard(self, cardsList, recruitInfo):
        ...
    def __onDisconnected(self):
        ...
    def __fillCardList(self):
        ...

class JunkTankmenWindow(WindowImpl):
    def __init__(self):
        ...
