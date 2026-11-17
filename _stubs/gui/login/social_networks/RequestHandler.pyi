# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/login/social_networks/RequestHandler.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import httplib as httplib
from urlparse import urlparse as urlparse, parse_qsl as parse_qsl
from BaseHTTPServer import BaseHTTPRequestHandler as BaseHTTPRequestHandler
from gui import GUI_SETTINGS as GUI_SETTINGS
from py2to3.compat import base64compat as base64compat
_TEMPLATE_EMPTY_GIF_BASE64 = 'R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=='

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        ...
    def onLogin(self, **kwargs):
        ...
    def onLoginWithRedirect(self, **kwargs):
        ...
    def __fetchParams(self, params):
        ...
    def log_request(self, code='-', size='-'):
        ...
