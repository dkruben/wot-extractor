# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/gf_notifications/gf_notification_inject.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from gui.shared.system_factory import collectGamefaceNotifications as collectGamefaceNotifications
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor as InjectComponentAdaptor
_logger: Any

class GFNotificationInject(InjectComponentAdaptor):
    __gfViewName: Any
    __isPopUp: Any
    __linkageData: Any
    def __init__(self, gfViewName, isPopUp, linkageData, *args, **kwargs):
        ...
    def _makeInjectView(self):
        ...

class PresentersFactory(object):
    @staticmethod
    def get(gfTemplate):
        ...
