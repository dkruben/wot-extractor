# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/hangar_crew_widget.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.hangar_crew_widget_model import HangarCrewWidgetModel as HangarCrewWidgetModel
from gui.impl.lobby.crew.widget.crew_widget import CrewWidget as CrewWidget
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.event_dispatcher import showPersonalCase as showPersonalCase, showChangeCrewMember as showChangeCrewMember
from gui.shared.gui_items.Tankman import NO_TANKMAN as NO_TANKMAN
from gui.shared.gui_items.Vehicle import NO_VEHICLE_ID as NO_VEHICLE_ID
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache

class HangarCrewWidget(ViewImpl):
    __slots__: tuple
    itemsCache: Any
    crewWidget: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def updateTankmen(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def __onWidgetSlotClick(self, tankmanID, slotIdx):
        ...
