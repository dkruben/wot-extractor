# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/battle_results/comp7_light_flag_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.lobby.battle_results.flag_view import FlagView as FlagView, _TEXTURE_PATH as _TEXTURE_PATH
from comp7_light.gui.impl.gen.view_models.views.lobby.battle_results.comp7_light_flag_view_model import Comp7LightFlagViewModel as Comp7LightFlagViewModel
from gui.impl.pub import WindowImpl as WindowImpl
from frameworks.wulf import WindowFlags as WindowFlags
from gui.impl.gen import R as R

class Comp7LightFlagWindow(WindowImpl):
    def __init__(self):
        ...

class Comp7LightFlagView(FlagView):
    _VIEW_SETTINGS_LAYOUT_ID: Any
    _VIEW_MODEL = Comp7LightFlagViewModel
    def _getLsmStateClass(self):
        ...
    @property
    def viewModel(self):
        ...
