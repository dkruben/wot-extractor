# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/platform/wgnp/demo_account/request.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from constants import WG_GAMES as WG_GAMES
from gui.platform.base.request import Params as Params, ContentType as ContentType
from gui.platform.wgnp.demo_account.response import WGNPDemoAccCredentialsAddResponse as WGNPDemoAccCredentialsAddResponse, WGNPDemoAccCredentialsConfirmResponse as WGNPDemoAccCredentialsConfirmResponse, WGNPDemoAccChangeNicknameResponse as WGNPDemoAccChangeNicknameResponse, WGNPDemoAccValidateNicknameResponse as WGNPDemoAccValidateNicknameResponse

class CredentialsStatusParams(Params):
    url = './personal/api/v2/account/credentials/basic/create/'
    method = 'GET'

class AddCredentialsParams(Params):
    response = WGNPDemoAccCredentialsAddResponse
    url = './personal/api/v2/account/credentials/basic/create/'
    headers: dict
    proofOfWorkURL = './personal/api/v2/account/credentials/basic/create/challenge/?type=pow'
    method = 'POST'
    queryParams: dict
    postData: dict
    def __init__(self, urlHost, login, password):
        ...

class ConfirmCredentialsParams(Params):
    response = WGNPDemoAccCredentialsConfirmResponse
    url = './personal/api/v2/account/credentials/basic/activate/'
    headers: dict
    method = 'POST'
    postData: dict
    def __init__(self, urlHost, code):
        ...

class NicknameStatusParams(Params):
    url = './personal/api/v2/account/name/update/state/'
    method = 'POST'

class ValidateNicknameParams(Params):
    response = WGNPDemoAccValidateNicknameResponse
    headers: dict
    url = './personal/account/nicknames/{nickname}/'
    postData: dict
    method = 'POST'
    auth = False
    addUserAgentHeader = False
    def __init__(self, urlHost, nickname):
        ...

class ChangeNicknameParams(Params):
    response = WGNPDemoAccChangeNicknameResponse
    url = './personal/api/v2/account/name/update/'
    headers: dict
    method = 'POST'
    postData: dict
    def __init__(self, urlHost, nickname, cost):
        ...
