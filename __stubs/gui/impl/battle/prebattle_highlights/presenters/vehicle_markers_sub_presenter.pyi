# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/battle/prebattle_highlights/presenters/vehicle_markers_sub_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import Math as Math
import typing as typing
import constants as constants
import nations as nations
from GUI import WGMarkerPositionController as WGMarkerPositionController
from frameworks.wulf.view.submodel_presenter import SubModelPresenter as SubModelPresenter
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.arena_info.arena_vos import isPremium as isPremium
from gui.battle_control.controllers.prebattle_highlights.pbh_constants import MARKER_X_FACTOR as MARKER_X_FACTOR, MARKER_Y_FACTOR as MARKER_Y_FACTOR
from gui.impl.gen.view_models.views.battle.prebattle_highlights.prebattle_highlights_marker_model import PrebattleHighlightsMarkerModel as PrebattleHighlightsMarkerModel
from gui.prestige.prestige_helpers import fillPrestigeEmblemModel as fillPrestigeEmblemModel
from helpers import dependency as dependency
from items import vehicles as vehicles
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from frameworks.wulf import Array as Array
from skeletons.gui.battle_session import IBattleContext as IBattleContext
from gui.battle_control.arena_info.arena_vos import VehicleArenaInfoVO as VehicleArenaInfoVO, VehicleTypeInfoVO as VehicleTypeInfoVO, PlayerInfoVO as PlayerInfoVO
from gui.impl.gen.view_models.common.user_name_model import UserNameModel as UserNameModel
from gui.impl.gen.view_models.common.badge_model import BadgeModel as BadgeModel
from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel as VehicleModel
from gui.impl.gen.view_models.views.lobby.prestige.prestige_emblem_model import PrestigeEmblemModel as PrestigeEmblemModel
from gui.battle_control.arena_info.player_format import PlayerFormatResult as PlayerFormatResult

class VehicleMarkersSubPresenter(SubModelPresenter):
    __sessionProvider: Any
    __vehiclesData: Any
    __markerCtrl: Any
    __battleContext: Any
    def __init__(self, viewModel, parentView):
        ...
    def packModel(self):
        ...
    def finalize(self):
        ...
    def __initMarkers(self):
        ...
    def __setVehicleInfo(self, model, vehicle):
        ...
    def __setPrestigeInfo(self, model, vehicle):
        ...
    def __setPlayerInfo(self, model, vehicle):
        ...
