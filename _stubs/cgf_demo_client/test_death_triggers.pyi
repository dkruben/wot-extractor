# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_demo_client/test_death_triggers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import CGF as CGF
import functools as functools
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from cgf_demo.demo_category import DEMO_CATEGORY as DEMO_CATEGORY
from DeathComponent import DeathComponent as DeathComponent
from Triggers import AreaTriggerComponent as AreaTriggerComponent
_logger: Any

# decorador original: @registerComponent
class TestAddDeathByTrigger(object):
    group = DEMO_CATEGORY
    editorTitle = 'Test Add Death by Trigger'
    domain = CGF.Domain.Client
    goLink: Any

# decorador original: @registerComponent
class TestRemoveDeathByTrigger(object):
    group = DEMO_CATEGORY
    editorTitle = 'Test Remove Death By Trigger'
    domain = CGF.Domain.Client
    goLink: Any

class TestDeathByTriggerSystem(CGF.System):
    AddDeathActivated: Any
    RemoveDeathActivated: Any
    DeathAccess: Any
    Reactions: Any
    def update(self):
        ...
    def __addDeath(self, go):
        ...
    def __removeDeath(self, go):
        ...
