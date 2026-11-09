# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/presenters/loadout_panel_presenter/battle_royale_loadout_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from helpers import dependency as dependency, time_utils as time_utils
from items import EQUIPMENT_TYPES as EQUIPMENT_TYPES
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.backport import createTooltipData as createTooltipData
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_royale_shell_model import BattleRoyaleShellModel as BattleRoyaleShellModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.loadout_view_model import LoadoutViewModel as LoadoutViewModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_royale_equipment_model import BattleRoyaleEquipmentModel as BattleRoyaleEquipmentModel
from battle_royale.gui.impl.lobby.br_helpers.respawn_ability import RespawnAbility as RespawnAbility
from battle_royale.gui.shared.event_dispatcher import showHangarVehicleConfigurator as showHangarVehicleConfigurator

# base nao representavel no stub: ViewComponent[...]
class BattleRoyaleLoadoutPresenter:
    __battleRoyaleController: Any
    __vehicle: Any
    def __init__(self, *args, **kwargs):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    @staticmethod
    def getTooltipData(event):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __updateModel(self, *_):
        ...
    def __setShells(self, vehicle, model):
        ...
    def __setEquipmentAndAbilities(self, vehicle, model):
        ...
    @staticmethod
    def __setRespawnAbility(respawn):
        ...
    @staticmethod
    def __showUpgrades():
        ...
    def update(self, vehicle):
        ...
