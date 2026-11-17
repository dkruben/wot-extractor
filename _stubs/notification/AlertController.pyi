# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/notification/AlertController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import Event as Event
from adisp import adisp_process as adisp_process
from gui import DialogsInterface as DialogsInterface
from gui.Scaleform.daapi.view.dialogs.SystemMessageMeta import SystemMessageMeta as SystemMessageMeta
from notification.BaseMessagesController import BaseMessagesController as BaseMessagesController

class AlertController(BaseMessagesController):
    __actualDisplayingAlerts: Any
    onAllAlertsClosed: Any
    def __init__(self, model):
        ...
    # decorador original: @adisp_process
    def showAlertMessage(self, notification):
        ...
    def isAlertShowing(self):
        ...
