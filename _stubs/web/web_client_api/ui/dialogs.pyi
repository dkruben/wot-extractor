# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/ui/dialogs.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.builtins import basestring as basestring
import adisp as adisp
import wg_async as wg_async
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from gui.shared.event_dispatcher import showPreformattedDialog as showPreformattedDialog
from shared_utils import first as first
from web.web_client_api import WebCommandException as WebCommandException, w2c as w2c, W2CSchema as W2CSchema, Field as Field

class _DialogSchema(W2CSchema):
    preset: Any
    title: Any
    message: Any
    buttons: Any
    focusedButton: Any
    btnDownSounds: Any

class DialogsWebApiMixin(object):
    # decorador original: @w2c(...)
    def showDialog(self, cmd):
        ...

def _dialogButtonsValidator(buttonsList, _=None):
    ...
