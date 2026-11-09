# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/pbs_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
import GenericComponents as GenericComponents
from cgf_script.registration import registerComponent as registerComponent

# decorador original: @registerComponent
class PostBattleBoardComponent(object):
    editorTitle = 'Post-battle Board'
    serialName = 'PostBattleBoardComponent'
    domain = CGF.Domain.ClientEditor

class PostBattleSystem(CGF.System):
    PostBattleActivated: Any
    PostBattleIterate: Any
    Reactions: Any
    _lastWrittenMapImage: Any
    def update(self):
        ...
    def __init__(self, *args):
        ...
    def onAdded(self, dynamicComp):
        ...
    def applyArenaImage(self, mapImageName):
        ...
