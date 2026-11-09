# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/mapbox/mapbox_survey_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import typing as typing
from constants import Configs as Configs
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer
from frameworks.wulf.view.array import fillStringsArray as fillStringsArray
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.mapbox.map_box_survey_view_model import MapBoxSurveyViewModel as MapBoxSurveyViewModel
from gui.impl.gen.view_models.views.lobby.mapbox.map_box_option_model import MapBoxOptionModel as MapBoxOptionModel
from gui.impl.gen.view_models.views.lobby.mapbox.map_box_question_model import QuestionType as QuestionType
from gui.impl.lobby.mapbox.sound import getMapboxViewSoundSpace as getMapboxViewSoundSpace
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow as LobbyWindow
from helpers import dependency as dependency, server_settings as server_settings, unicodeToStr as unicodeToStr
from skeletons.gui.game_control import IMapboxController as IMapboxController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from soft_exception import SoftException as SoftException
from gui.impl.gen.view_models.views.lobby.mapbox.map_box_question_model import MapBoxQuestionModel as MapBoxQuestionModel
from gui.impl.gen.view_models.views.lobby.mapbox.map_box_answers_model import MapBoxAnswersModel as MapBoxAnswersModel
from gui.mapbox.mapbox_survey_helper import Question as Question

class MapBoxSurvey(ViewImpl):
    __slots__: tuple
    _COMMON_SOUND_SPACE: Any
    __mapboxCtrl: Any
    __lobbyContext: Any
    __mapName: Any
    __closeCallback: Any
    def __init__(self, mapName, closeCallback):
        ...
    @property
    def viewModel(self):
        ...
    def _initialize(self):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    # decorador original: @server_settings.serverSettingsChangeListener(...)
    def __onServerSettingsChanged(self, _):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    def __updateViewModel(self, question):
        ...
    def __fillQuestionModel(self, model, question):
        ...
    def __fillAnswers(self, model, question, optionId=None):
        ...
    def __fillOptions(self, model, question):
        ...
    def __updateSelectedVariants(self, model, questionId, optionId=None):
        ...
    def __onConfirmCompletion(self):
        ...
    def __onClose(self):
        ...
    def __onShowPreviousPage(self):
        ...
    def __onShowNextPage(self):
        ...
    def __onAnswerQuestion(self, args):
        ...
    def __setFinalScreen(self):
        ...

class MapBoxSurveyWindow(LobbyWindow):
    __slots__: tuple
    def __init__(self, mapName, closeCallback=None):
        ...
