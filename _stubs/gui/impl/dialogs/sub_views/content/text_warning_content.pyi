# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/dialogs/sub_views/content/text_warning_content.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.dialogs.dialog_template_utils import toString as toString
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.common.dialogs.sub_views.text_with_warning_view_model import TextWithWarningViewModel as TextWithWarningViewModel
from gui.impl.pub import ViewImpl as ViewImpl

class TextWithWarning(ViewImpl):
    __slots__: tuple
    def __init__(self, mainText, warningText=None):
        ...
    def _onLoading(self, mainText, warningText, *args, **kwargs):
        ...
    def updateText(self, text):
        ...
