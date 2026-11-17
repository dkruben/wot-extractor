# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/impl/battle/battle_page/respawn_ammunition_panel_inject.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from frontline.gui.battle_control.controllers.frontline_respawn_ctrl import IFrontlineRespawnView as IFrontlineRespawnView
from frontline.gui.impl.battle.battle_page.respawn_ammunition_panel_view import RespawnAmmunitionPanelView as RespawnAmmunitionPanelView
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor as InjectComponentAdaptor, hasAliveInject as hasAliveInject
from frontline.gui.battle_control.controllers.base_respawn_ctrl import IRespawnView as IRespawnView
from gui.battle_control.gui_vehicle_builder import VehicleBuilder as VehicleBuilder
from gui.shared.gui_items.artefacts import BattleAbility as BattleAbility
from gui.veh_post_progression.sounds import playSound as playSound, Sounds as Sounds
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController
from skeletons.gui.shared.gui_items import IGuiItemsFactory as IGuiItemsFactory

class RespawnAmmunitionPanelInject(InjectComponentAdaptor, IRespawnView):
    __slots__: tuple
    __itemsFactory: Any
    __sessionProvider: Any
    _vehicle: Any
    def __init__(self):
        ...
    def show(self, selectedID, vehs, cooldowns, limits=0):
        ...
    def hide(self):
        ...
    # decorador original: @hasAliveInject(...)
    def setRespawnInfoExt(self, vehInfo, setupIndexes):
        ...
    def _onPopulate(self):
        ...
    def _addInjectContentListeners(self):
        ...
    def _removeInjectContentListeners(self):
        ...
    def _makeInjectView(self, vehicle):
        ...
    def _updateGuiVehicle(self, vehicleInfo, setupIndexes):
        ...
    def __onSwitchLayout(self, vehCD, groupID, layoutIdx):
        ...
    def __needVehicleInvalidation(self, vehicleInfo, setupIndexes):
        ...

class FrontlineRespawnAmmunitionPanelInject(RespawnAmmunitionPanelInject, IFrontlineRespawnView):
    __epicController: Any
    def _updateGuiVehicle(self, vehicleInfo, setupIndexes):
        ...
