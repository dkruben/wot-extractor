# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/account_completion/common/field_email_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.gen.view_models.views.lobby.account_completion.common.base_field_model import BaseFieldModel as BaseFieldModel

class FieldEmailModel(BaseFieldModel):
    __slots__: tuple
    EMAIL_LEN_MAX = 50
    EMAIL_LEN_MIN = 4
    onErrorTimer: Any
    def __init__(self, properties=5, commands=3):
        ...
    def getErrorTime(self):
        ...
    def setErrorTime(self, value):
        ...
    def _initialize(self):
        ...
