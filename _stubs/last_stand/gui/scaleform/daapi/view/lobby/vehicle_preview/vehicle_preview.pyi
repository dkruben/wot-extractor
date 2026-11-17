# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/lobby/vehicle_preview/vehicle_preview.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import BigWorld as BigWorld
from HeroTank import HeroTank as HeroTank
from gui.Scaleform.daapi.view.lobby.vehicle_preview.vehicle_preview import VehiclePreview as VehiclePreview
from gui.hangar_cameras.hangar_camera_common import CameraMovementStates as CameraMovementStates, CameraRelatedEvents as CameraRelatedEvents
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.event_dispatcher import showVehPostProgressionView as showVehPostProgressionView
from last_stand.gui.scaleform.genConsts.LAST_STAND_HANGAR_ALIASES import LAST_STAND_HANGAR_ALIASES as LAST_STAND_HANGAR_ALIASES
from last_stand.gui.shared.event_dispatcher import showHeroTankPreview as showHeroTankPreview, showHangar as showHangar
from last_stand.gui.sounds import playSound as playSound
from last_stand.gui.sounds.sound_constants import LS_PREVIEW_ENTER as LS_PREVIEW_ENTER, LS_PREVIEW_EXIT as LS_PREVIEW_EXIT, HANGAR_SOUND_SETTINGS as HANGAR_SOUND_SETTINGS

class LSVehiclePreview(VehiclePreview, IGlobalListener):
    _COMMON_SOUND_SPACE = HANGAR_SOUND_SETTINGS
    def onGoToPostProgressionClick(self):
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
