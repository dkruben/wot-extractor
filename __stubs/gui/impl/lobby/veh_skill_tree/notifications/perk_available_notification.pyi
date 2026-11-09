# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/veh_skill_tree/notifications/perk_available_notification.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import VEH_SKILL_TREE_POPUP_SHOWN as VEH_SKILL_TREE_POPUP_SHOWN
from helpers import dependency as dependency
from gui.impl.gen.view_models.views.lobby.veh_skill_tree.notifications.perk_available_view_model import PerkAvailableViewModel as PerkAvailableViewModel
from gui.impl.lobby.common.vehicle_model_helpers import fillVehicleModel as fillVehicleModel
from gui.impl.lobby.gf_notifications import NotificationBase as NotificationBase
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.prb_control.settings import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG
from gui.shared.event_dispatcher import showVehicleHubVehSkillTree as showVehicleHubVehSkillTree
from skeletons.gui.shared import IItemsCache as IItemsCache
TRAINING_FLAGS: Any

class PerkAvailableNotification(IGlobalListener, NotificationBase):
    __itemsCache: Any
    __vehCD: Any
    def __init__(self, resId, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _update(self):
        ...
    def _getEvents(self):
        ...
    def __onClose(self):
        ...
    def __onGoToProgression(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def onPrbEntitySwitched(self):
        ...
    def onUnitPlayerRemoved(self, pInfo):
        ...
    def onUnitPlayerStateChanged(self, pInfo):
        ...
    def __isButtonDisabled(self):
        ...
