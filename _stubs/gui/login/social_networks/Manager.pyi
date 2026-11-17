# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/login/social_networks/Manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from gui import GUI_SETTINGS as GUI_SETTINGS
from connection_mgr import CONNECTION_METHOD as CONNECTION_METHOD
from gui.login.Manager import Manager as CredentialsLoginManager
from .WebBridge import WebBridge as WebBridge

class SOCIAL_NETWORKS(object):
    FACEBOOK = 'facebook'
    GOOGLE = 'google'
    WGNI = 'wgni'
    VKONTAKTE = 'vkontakte'
    YAHOO = 'yahoo'
    NAVER = 'naver'
    TWITTER = 'twitter'
    ODNOKLASSNIKI = 'odnoklassniki'

class Manager(CredentialsLoginManager):
    __webBridge: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def initiateSocialLogin(self, socialNetworkName, serverName, rememberUser, isRegistration):
        ...
    @staticmethod
    def getAvailableSocialNetworks():
        ...
