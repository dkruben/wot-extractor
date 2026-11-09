# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/crew_showcase_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import WindowFlags as WindowFlags, ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.lobby.mapbox.sound import playSound as playSound
from gui.impl.pub.lobby_window import LobbyWindow as LobbyWindow
from gui.server_events.awards_formatters import AWARDS_SIZES as AWARDS_SIZES
from gui.server_events.recruit_helper import getRecruitInfo as getRecruitInfo
from halloween.gui.impl.gen.view_models.views.lobby.crew_member_view_model import CrewMemberViewModel as CrewMemberViewModel, CrewStates as CrewStates
from halloween.gui.impl.gen.view_models.views.lobby.crew_showcase_view_model import CrewShowcaseViewModel as CrewShowcaseViewModel
from halloween.gui.impl.lobby.base_view import BaseView as BaseView
from halloween.gui.impl.lobby.hw_helpers import HalloweenBonusesAwardsComposer as HalloweenBonusesAwardsComposer
from halloween.gui.impl.lobby.hw_helpers.bonuses_formatters import getHWTwitchAwardFormatter as getHWTwitchAwardFormatter, getImgName as getImgName
from halloween.gui.shared.event_dispatcher import showHalloweenShopBundle as showHalloweenShopBundle
from halloween.gui.sounds.sound_constants import CREW_SHOWCASE_ENTER as CREW_SHOWCASE_ENTER, CREW_SHOWCASE_EXIT as CREW_SHOWCASE_EXIT
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController as IHalloweenArtefactsController
from halloween.skeletons.halloween_twitch_con_controller import IHalloweenTwitchConController as IHalloweenTwitchConController
from helpers import dependency as dependency
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from skeletons.gui.game_control import ISpecialSoundCtrl as ISpecialSoundCtrl
from skeletons.gui.impl import IGuiLoader as IGuiLoader

class CrewShowcaseView(BaseView):
    _MAX_BONUSES_IN_VIEW = 1
    _guiLoader: Any
    _hwArtifactsCtrl: Any
    _hwTwitchCtrl: Any
    _specialSounds: Any
    __bonusCache: Any
    __idGen: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __fillViewModel(self):
        ...
    def __getStatus(self, commander):
        ...
    def __onClose(self):
        ...
    def __onShop(self, args=None):
        ...
    def __updateTwitch(self):
        ...
    def __onPlaySound(self, args=None):
        ...

class CrewShowcaseWindow(LobbyWindow):
    def __init__(self, parent=None):
        ...
