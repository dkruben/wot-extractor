# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/tutorial/doc_loader/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import ResMgr as ResMgr
from tutorial import settings as settings
from tutorial.doc_loader import gui_config as gui_config
from tutorial.doc_loader.parsers import DescriptorParser as DescriptorParser, ChapterParser as ChapterParser
from tutorial.logger import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION

def loadDescriptorData(setting, exParsers=None, clearCache=False):
    ...
def loadChapterData(chapter, chapterParser, initial=False):
    ...
def clearChapterData(chapter):
    ...
