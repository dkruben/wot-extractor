# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/dialogs/widgets/warning_text.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.dialogs.dialog_template_utils import toString as toString
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.dialogs.sub_views.simple_text_view_model import SimpleTextViewModel as SimpleTextViewModel
from gui.impl.pub import ViewImpl as ViewImpl

class WarningText(ViewImpl):
    __slots__: tuple
    LAYOUT_DYN_ACCESSOR = R.views.dialogs.widgets.WarningText
    __text: Any
    def __init__(self, text, layoutID=None):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __updateViewModel(self):
        ...
