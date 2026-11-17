# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/award_congrats_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow, createTooltipData as createTooltipData
from gui.impl.gen import R as R
from halloween.gui.impl.gen.view_models.views.lobby.award_congrats_view_model import AwardCongratsViewModel as AwardCongratsViewModel
from halloween.gui.impl.lobby.base_view import BaseView as BaseView, HWLobbyWindow as HWLobbyWindow
from halloween.gui.impl.lobby.hw_helpers import fillRewardsCommon as fillRewardsCommon, getEndingToken as getEndingToken
from halloween.gui.sounds import playSound as playSound
from halloween.gui.sounds.sound_constants import AwardCongratsWindowSounds as AwardCongratsWindowSounds
from helpers import dependency as dependency
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController as IHalloweenArtefactsController
_R_BACKPORT_TOOLTIP: Any

class AwardCongratsView(BaseView):
    __slots__: tuple
    layoutID: Any
    _MAX_BONUSES_IN_VIEW = 1
    _hwArtefactsCtrl: Any
    _choiceID: Any
    __idGen: Any
    __bonusCache: Any
    def __init__(self, choiceID, layoutID=None):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTip(self, event):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _onLoading(self):
        ...
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def __onClose(self):
        ...

class AwardCongratsViewWindow(HWLobbyWindow):
    _args: Any
    def __init__(self, layoutID, choiceID, parent=None):
        ...
