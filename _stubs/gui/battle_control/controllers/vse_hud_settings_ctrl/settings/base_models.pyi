# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/vse_hud_settings_ctrl/settings/base_models.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from helpers import i18n as i18n
from pve_battle_hud import getPveHudLogger as getPveHudLogger
_logger: Any

class BaseClientModel(object):
    ...

class TextClientModel(BaseClientModel):
    # decorador original: @validateTemplateKey
    def _getText(self, templateKey):
        ...
    # decorador original: @validateTemplateKey
    def _getPluralText(self, templateKey, params):
        ...

def validateTemplateKey(func):
    ...
def _normalizeParams(text, params):
    ...
