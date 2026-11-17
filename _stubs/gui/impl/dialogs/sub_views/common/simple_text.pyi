# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/dialogs/sub_views/common/simple_text.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
import typing as typing
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.dialogs.dialog_template_utils import toString as toString
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.dialogs.sub_views.image_substitution_view_model import ImageSubstitutionViewModel as ImageSubstitutionViewModel
from gui.impl.gen.view_models.views.dialogs.sub_views.simple_text_view_model import SimpleTextViewModel as SimpleTextViewModel
from gui.impl.pub import ViewImpl as ViewImpl
from typing import Optional as Optional, List as List, Union as Union
from frameworks.wulf import PyResAccessor as PyResAccessor
ImageSubstitution: Any

class SimpleText(ViewImpl):
    __slots__: tuple
    _LAYOUT_DYN_ACCESSOR = R.views.dialogs.sub_views.common.SimpleText
    def __init__(self, text, imageSubstitutions=None, layoutID=None):
        ...
    def _onLoading(self, text, imageSubstitutions, *args, **kwargs):
        ...
    def updateText(self, text):
        ...
