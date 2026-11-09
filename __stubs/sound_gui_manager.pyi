# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/sound_gui_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
CommonSoundSpaceSettings: Any

class ViewSoundExtension(object):
    __commonSoundManagers: dict
    __soundSpace: Any
    __soundsManager: Any
    __parentManager: Any
    def __init__(self, soundSpace):
        ...
    @property
    def soundManager(self):
        ...
    def startSoundSpace(self):
        ...
    def initSoundManager(self):
        ...
    def destroySoundManager(self):
        ...
