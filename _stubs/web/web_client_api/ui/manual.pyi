# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/ui/manual.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.doc_loaders.manual_xml_data_reader import getPagesIndexesList as getPagesIndexesList
from helpers import dependency as dependency
from skeletons.gui.game_control import IManualController as IManualController
from web.web_client_api import W2CSchema as W2CSchema, w2c as w2c, Field as Field

class _OpenManualWindowSchema(W2CSchema):
    ignore_chapter: Any
    chapter_index: Any

class ManualPageWebApiMixin(object):
    manualController: Any
    # decorador original: @w2c(...)
    def openManualPage(self, cmd):
        ...

def _chapterIndexValidator(key, _):
    ...
