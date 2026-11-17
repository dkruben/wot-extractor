# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/dialogs/SystemMessageMeta.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from gui.Scaleform.daapi.view.dialogs import IDialogMeta as IDialogMeta
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared import events as events
from soft_exception import SoftException as SoftException
SessionControlAuxData: Any

class SESSION_CONTROL_TYPE(object):
    AOGAS = 'AOGAS'
    KOREA_PARENTAL_CONTROL = 'KOREA_PARENTAL_CONTROL'

class SystemMessageMeta(IDialogMeta):
    __notificationVO: Any
    __settingsVO: Any
    __title: Any
    __cancelLabel: Any
    def __init__(self, notification):
        ...
    def getSettings(self):
        ...
    def getMessageObject(self):
        ...
    def getEventType(self):
        ...
    def getTitle(self):
        ...
    def getCancelLabel(self):
        ...
    def cleanUp(self):
        ...
    def getViewScopeType(self):
        ...
