# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/presenters/loadout_panel_presenter/commander_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.gen import R as R
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from helpers import dependency as dependency
from items.tankmen import ROLES_BY_SKILLS as ROLES_BY_SKILLS
from shared_utils import first as first
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController
from battle_royale.gui.impl.lobby.br_helpers.utils import setEventInfo as setEventInfo
from battle_royale.gui.impl.gen.view_models.views.lobby.views.commander_view_model import CommanderViewModel as CommanderViewModel, CommanderPerkModel as CommanderPerkModel

# base nao representavel no stub: ViewComponent[...]
class CommanderPresenter:
    __battleRoyaleController: Any
    __appLoader: Any
    __toolTipMgr: Any
    __vehicle: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTip(self, event):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __updateModel(self):
        ...
    def __getCommanderID(self):
        ...
    def update(self, vehicle):
        ...
