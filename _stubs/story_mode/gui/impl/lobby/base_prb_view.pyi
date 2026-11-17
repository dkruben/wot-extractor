# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/impl/lobby/base_prb_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from logging import getLogger as getLogger
from adisp import adisp_process as adisp_process
from gui.impl.pub import ViewImpl as ViewImpl
from gui.prb_control.dispatcher import g_prbLoader as g_prbLoader
from gui.prb_control.entities.base.ctx import PrbAction as PrbAction
from gui.prb_control.settings import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from story_mode.skeletons.story_mode_controller import IStoryModeController as IStoryModeController
from frameworks.wulf import ViewSettings as ViewSettings, ViewFlags as ViewFlags
from story_mode_common.story_mode_constants import LOGGER_NAME as LOGGER_NAME
_logger: Any

class BasePrbView(ViewImpl):
    LAYOUT_ID = None
    MODEL_CLASS = None
    _storyModeCtrl: Any
    _appLoader: Any
    def __init__(self, *_, **__):
        ...
    # decorador original: @adisp_process
    def _quit(self):
        ...
