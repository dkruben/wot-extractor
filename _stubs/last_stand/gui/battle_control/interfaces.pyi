# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/battle_control/interfaces.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.battle_control.arena_info.interfaces import IArenaLoadController as IArenaLoadController

class ILSVOIPController(IArenaLoadController):
    __slots__: tuple
    @property
    def isVoipSupported(self):
        ...
    @property
    def isVoipEnabled(self):
        ...
    @property
    def isTeamChannelAvailable(self):
        ...
    @property
    def isJoined(self):
        ...
    @property
    def isTeamVoipEnabled(self):
        ...
    def toggleChannelConnection(self):
        ...
