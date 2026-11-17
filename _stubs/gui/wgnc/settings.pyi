# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/wgnc/settings.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

WGNC_POP_UP_PRIORITIES: tuple
WGNC_POP_UP_BUTTON_WIDTH = 107
WGNC_GUI_INVALID_SEQS: tuple
WGNC_DEFAULT_ICON = 'InformationIcon'
_WGNC_ICON_TO_LOCAL: dict
_WGNC_BG_TO_LOCAL: dict

class WGNC_GUI_TYPE(object):
    UNDEFINED = 0
    POP_UP = 1
    BASIC_WINDOW = 2
    COMPLEX_WINDOW = 4
    BROWSER = 8

class WGNC_DATA_PROXY_TYPE(object):
    UNDEFINED = 0
    CLAN_APP = 1
    CLAN_INVITE = 2
    CLAN_APP_DECLINED = 4
    CLAN_APP_ACCEPTED = 8
    SHOW_IN_BROWSER = 11
    CLAN_INVITE_ACCEPTED = 16
    CLAN_INVITE_DECLINED = 18
    CLAN_INVITES_CREATED = 20
    CLAN_APP_DECLINED_FOR_MEMBERS = 24
    CLAN_APP_ACCEPTED_FOR_MEMBERS = 32
    SHOW_PROMO_TEASER = 64
    UPDATE_REFERRAL_BUBBLE = 80
    BECOME_RECRUITER = 81
    SHOW_REFERRAL_WINDOW = 82
    UPDATE_CLAN_NOTIFICATION = 96
    PAYMENT_METHOD_CHANGE_NOTIFICATION = 128
    MAPBOX_SURVEY_AVAILABLE_NOTIFICATION = 144
    MAPBOX_EVENT_STARTED_NOTIFICATION = 145
    MAPBOX_EVENT_ENDED_NOTIFICATION = 146
    MAPBOX_REWARD_RECEIVED_NOTIFICATION = 148
    INTEGRATED_AUCTION_RATE_ERROR = 256
    INTEGRATED_AUCTION_RATE_LOST = 257
    INTEGRATED_AUCTION_RATE_BELOW_COMPETITIVE = 258
    CLAN_SUPPLY_QUEST_UPDATE = 259

def convertToLocalIcon(icon):
    ...
def convertToLocalBG(icon):
    ...
