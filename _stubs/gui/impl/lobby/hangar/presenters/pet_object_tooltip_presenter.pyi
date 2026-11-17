# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/presenters/pet_object_tooltip_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl import backport as backport
from gui.impl.auxiliary.tooltips.simple_tooltip import createSimpleTooltip as createSimpleTooltip
from gui.impl.gen.view_models.views.lobby.hangar.sub_views.pet_object_tooltip_model import PetObjectTooltipModel as PetObjectTooltipModel
from gui.impl.lobby.pet_system.tooltips.pet_storage_tooltip import PetStorageTooltip as PetStorageTooltip
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.pet_system.constants import EVENT_NAME_FORMAT as EVENT_NAME_FORMAT
from gui.pet_system.pet_item_helper import PetItem as PetItem
from gui.pet_system.requester import INVALID_EVENT_ID as INVALID_EVENT_ID, INVALID_PET_ID as INVALID_PET_ID
from gui.shared import g_eventBus as g_eventBus
from gui.shared.event_bus import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import PetObjectHoverEvent as PetObjectHoverEvent, PetSystemEvent as PetSystemEvent
from helpers import dependency as dependency
from pet_system_common.pet_constants import PetHangarObject as PetHangarObject, PetStateBehavior as PetStateBehavior
from gui.impl.gen import R as R
from skeletons.gui.pet_system import IPetSystemController as IPetSystemController

class _Tooltips(object):
    NONE = ''
    STORAGE = 'storageTooltip'
    EVENT = 'eventTooltip'

# base nao representavel no stub: ViewComponent[...]
class PetObjectTooltipPresenter:
    __petController: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def createToolTip(self, event):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getListeners(self):
        ...
    def __onHoverInEvent(self, event):
        ...
    def __getTooltipToShow(self, hoveredObj):
        ...
    def __onHoverOutEvent(self, _):
        ...
