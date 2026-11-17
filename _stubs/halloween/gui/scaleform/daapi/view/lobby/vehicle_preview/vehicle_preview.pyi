# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/lobby/vehicle_preview/vehicle_preview.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from HeroTank import HeroTank as HeroTank
from gui.Scaleform.daapi.view.lobby.vehicle_preview.vehicle_preview import VehiclePreview as VehiclePreview
from gui.Scaleform.genConsts.VEHPREVIEW_CONSTANTS import VEHPREVIEW_CONSTANTS as VEHPREVIEW_CONSTANTS
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.hangar_cameras.hangar_camera_common import CameraMovementStates as CameraMovementStates, CameraRelatedEvents as CameraRelatedEvents
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.event_dispatcher import showVehPostProgressionView as showVehPostProgressionView
from halloween.gui.scaleform.genConsts.HALLOWEEN_HANGAR_ALIASES import HALLOWEEN_HANGAR_ALIASES as HALLOWEEN_HANGAR_ALIASES
from halloween.gui.shared.event_dispatcher import showHeroTankPreview as showHeroTankPreview, showHangar as showHangar
from halloween.gui.sounds import playSound as playSound
from halloween.gui.sounds.sound_constants import HW_PREVIEW_ENTER as HW_PREVIEW_ENTER, HW_PREVIEW_EXIT as HW_PREVIEW_EXIT, HANGAR_SOUND_SETTINGS as HANGAR_SOUND_SETTINGS

class HWVehiclePreview(VehiclePreview, IGlobalListener):
    _COMMON_SOUND_SPACE = HANGAR_SOUND_SETTINGS
    __ctx: Any
    def __init__(self, ctx=None):
        ...
    def setBottomPanel(self):
        ...
    def closeView(self):
        ...
    def handleSelectedEntityUpdated(self, event):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _processBackClick(self, ctx=None):
        ...
    def onGoToPostProgressionClick(self):
        ...
