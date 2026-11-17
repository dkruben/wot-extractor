# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/platform/wgnp/steam_account/request.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from constants import WG_GAMES as WG_GAMES
from gui.platform.base.request import Params as Params
from gui.platform.wgnp.steam_account.response import WGNPSteamAccEmailAddResponse as WGNPSteamAccEmailAddResponse, WGNPSteamAccEmailConfirmResponse as WGNPSteamAccEmailConfirmResponse

class EmailStatusParams(Params):
    url = './personal/api/v2/account/email/state/'
    headers: dict
    method = 'POST'

class AddEmailParams(Params):
    response = WGNPSteamAccEmailAddResponse
    url = './personal/api/v2/account/email/create/'
    headers: dict
    proofOfWorkURL = './personal/api/v2/account/email/create/challenge/?type=pow'
    method = 'POST'
    queryParams: dict
    postData: dict
    def __init__(self, urlHost, email):
        ...

class ConfirmEmailParams(Params):
    response = WGNPSteamAccEmailConfirmResponse
    url = './personal/api/v2/account/email/activate/'
    headers: dict
    method = 'POST'
    def __init__(self, urlHost, code):
        ...
