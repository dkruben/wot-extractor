# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/processors/winback.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
from gui import SystemMessages as SystemMessages
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.SystemMessages import SM_TYPE as SM_TYPE
from gui.impl import backport as backport
from gui.impl.dialogs.dialogs import showSingleDialogWithResultData as showSingleDialogWithResultData
from gui.impl.gen import R as R
from gui.shared.gui_items.processors import Processor as Processor, plugins as plugins
from typing import Optional as Optional
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogBaseView as FullScreenDialogBaseView
from frameworks import wulf as wulf
_WINBACK_MESSAGES = R.strings.system_messages.winback

class WinbackTurnOffBattlesProcessor(Processor):
    __reason: Any
    def __init__(self, reason, dialog=None, parent=None):
        ...
    def _request(self, callback):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
