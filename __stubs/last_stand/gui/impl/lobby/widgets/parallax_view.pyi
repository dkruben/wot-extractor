# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/widgets/parallax_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import logging as logging
import typing as typing
import ResMgr as ResMgr
from gui.impl.gen import R as R
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.shared.utils.graphics import isLowPreset as isLowPreset
from helpers import dependency as dependency
from last_stand.gui.impl.gen.view_models.views.lobby.widgets.parallax_view_model import ParallaxViewModel as ParallaxViewModel
from last_stand.skeletons.ls_controller import ILSController as ILSController
from last_stand.skeletons.ls_story_point_controller import ILSStoryPointController as ILSStoryPointController
from last_stand.gui.impl.gen.view_models.views.lobby.widgets.parallax_model import ParallaxModel as ParallaxModel
_logger: Any
PATH_TO_CONFIGS = 'last_stand/gui/parallax/configs.json'
PARALLAX_DEFAULT_SCALE = 1

# base nao representavel no stub: ViewComponent[...]
class ParallaxView:
    lsCtrl: Any
    lsStoryPointCtrl: Any
    _parallaxConfig: Any
    _currentSlideID: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def __onSlide(self, args):
        ...
    def __readParallaxConfig(self, currentSlideID):
        ...

def _readSection(path):
    ...
def _toJson(inputData):
    ...
def _getChunks(count, name, path):
    ...
