# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/battle/death_cam/death_cam_hud_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from gui.impl.battle.death_cam.death_cam_ui_view import DeathCamUIView as DeathCamUIView
from gui.impl.battle.death_cam.marker_view import DeathCamMarkerView as DeathCamMarkerView
from gui.impl.gen import R as R
from typing import List as List, Union as Union
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.impl.gen.view_models.views.battle.death_cam.death_cam_hud_view_model import DeathCamHudViewModel as DeathCamHudViewModel
from gui.impl.pub import ViewImpl as ViewImpl
_logger: Any

class DeathCamHudView(ViewImpl):
    __slots__: tuple
    __subviews: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
