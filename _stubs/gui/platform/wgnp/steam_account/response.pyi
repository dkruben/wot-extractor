# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/platform/wgnp/steam_account/response.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.platform.base.response import PlatformResponse as PlatformResponse

class WGNPSteamEmailActionResponse(PlatformResponse):
    @property
    def isAccountAlreadyHasEmail(self):
        ...
    @property
    def isEmailAlreadyTaken(self):
        ...

class WGNPSteamAccEmailAddResponse(WGNPSteamEmailActionResponse):
    @property
    def requestRestrictedUntilTime(self):
        ...
    @property
    def isEmailInvalid(self):
        ...
    @property
    def isEmailForbidden(self):
        ...
    @property
    def isEmailMinLength(self):
        ...
    @property
    def isEmailMaxLength(self):
        ...
    @property
    def isEmailBannedInCountry(self):
        ...
    @property
    def isEmailRestrictedByCountry(self):
        ...
    @property
    def isRequestLimitExceeded(self):
        ...

class WGNPSteamAccEmailConfirmResponse(WGNPSteamEmailActionResponse):
    @property
    def isConfirmationCodeIncorrect(self):
        ...
    @property
    def isConfirmationCodeDeactivated(self):
        ...
    @property
    def isConfirmationCodeExpired(self):
        ...
