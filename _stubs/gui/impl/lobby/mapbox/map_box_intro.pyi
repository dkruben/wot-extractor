# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/mapbox/map_box_intro.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import Configs as Configs
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.mapbox.map_box_intro_model import MapBoxIntroModel as MapBoxIntroModel
from gui.impl.lobby.mapbox.sound import getMapboxViewSoundSpace as getMapboxViewSoundSpace
from gui.impl.pub import ViewImpl as ViewImpl
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.prb_control.settings import SELECTOR_BATTLE_TYPES as SELECTOR_BATTLE_TYPES
from gui.server_events.events_dispatcher import showMissionsMapboxProgression as showMissionsMapboxProgression
from gui.shared.event_dispatcher import showModeSelectorWindow as showModeSelectorWindow
from gui.shared.utils import SelectorBattleTypesUtils as SelectorBattleTypesUtils
from helpers import dependency as dependency, server_settings as server_settings, time_utils as time_utils
from skeletons.gui.game_control import IMapboxController as IMapboxController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext

class MapBoxIntro(ViewImpl, IGlobalListener):
    __slots__: tuple
    _COMMON_SOUND_SPACE: Any
    __mapboxCtrl: Any
    __lobbyContext: Any
    __closeCallback: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def onPrbEntitySwitched(self):
        ...
    def _initialize(self):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __onPrimeTimeChanged(self, *_):
        ...
    # decorador original: @server_settings.serverSettingsChangeListener(...)
    def __onServerSettingsChanged(self, _):
        ...
    def __updateViewModel(self):
        ...
    def __onClose(self):
        ...
