# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/account_completion/confirm_credentials_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.account_completion.common.base_field_model import BaseFieldModel as BaseFieldModel
from gui.impl.gen.view_models.views.lobby.account_completion.common.base_wgnp_overlay_view_model import BaseWgnpOverlayViewModel as BaseWgnpOverlayViewModel

class ConfirmCredentialsModel(BaseWgnpOverlayViewModel):
    __slots__: tuple
    onResendClicked: Any
    def __init__(self, properties=13, commands=5):
        ...
    @property
    def field(self):
        ...
    @staticmethod
    def getFieldType():
        ...
    def getTimer(self):
        ...
    def setTimer(self, value):
        ...
    def getEmail(self):
        ...
    def setEmail(self, value):
        ...
    def getResendButtonLabel(self):
        ...
    def setResendButtonLabel(self, value):
        ...
    def _initialize(self):
        ...
