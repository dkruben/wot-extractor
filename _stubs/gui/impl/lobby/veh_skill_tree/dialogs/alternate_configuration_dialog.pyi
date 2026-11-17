# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/veh_skill_tree/dialogs/alternate_configuration_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
from functools import partial as partial
import BigWorld as BigWorld
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.auxiliary.vehicle_helper import fillVehicleInfo as fillVehicleInfo
from gui.impl.gen import R as R
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogBaseView as FullScreenDialogBaseView
from gui.impl.lobby.veh_post_progression.tooltips.setup_tooltip_view import SetupTooltipView as SetupTooltipView
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.items_actions import factory as factory
from helpers import dependency as dependency
from items import vehicles as vehicles
from post_progression_common import ACTION_TYPES as ACTION_TYPES, GROUP_ID_BY_FEATURE as GROUP_ID_BY_FEATURE
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.veh_skill_tree import alternate_configuration_dialog_model as alternate_configuration_dialog_model
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.veh_skill_tree import alternate_configuration_dialog_loadout_model as alternate_configuration_dialog_loadout_model
_FEATURE_TO_LOADOUT_TYPE: dict
_LOADOUT_TYPE_TO_FEATURE: dict

class AlternateConfigurationDialog(FullScreenDialogBaseView):
    __itemsCache: Any
    __vehicle: Any
    __feature: Any
    __nodeID: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _onLoading(self, vehIntCD, feature, nodeID, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def __onInventoryResync(self, reason, diff):
        ...
    def __onClose(self):
        ...
    # decorador original: @args2params(...)
    def __onAffirmate(self, loadoutStates):
        ...
    def __switchPrebattleAmmoPanelAvailability(self, groupID, newState):
        ...
    def __update(self):
        ...
    def __fillLoadouts(self, viewModel):
        ...
    def __fillLoadout(self, loadouts, featureName):
        ...
