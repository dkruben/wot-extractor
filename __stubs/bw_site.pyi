# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/bw_site.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import os as os
import traceback as traceback
import sys as sys
import pydoc as pydoc
import fnmatch as fnmatch
import logging as logging
import BigWorld as BigWorld
import BWLogging as BWLogging
import BWUtil as BWUtil
import ResMgr as ResMgr
import bwdeprecations as bwdeprecations
from bwdebug import NOTICE_MSG as NOTICE_MSG
import builtins as builtins
import __builtin__ as builtins
import BWAutoImport as BWAutoImport
DEFAULT_ENCODING = 'utf-8'
PLATFORM_SUFFIX: Any
NOARCH_SUFFIX: Any

class _Helper(object):
    def __repr__(self):
        ...
    def __call__(self, *args, **kwds):
        ...

def set_helper():
    ...
def set_default_encoding():
    ...
def resMgrListDir(path, fnpat=None):
    ...
def resMgrDirExists(path):
    ...
def getsitepackages():
    ...
def _init_pathinfo():
    ...
def addpackage(sitedir, name, known_paths):
    ...
def addsitedir(sitedir, known_paths=None):
    ...
def addsitepackages(known_paths):
    ...
def setup_paths():
    ...
# decorador original: @BWUtil.if_only_component(...)
def set_twisted_reactor():
    ...
def set_builtin_open_patch():
    ...
# decorador original: @BWUtil.if_only_component(...)
def revert_builtin_open_patch():
    ...
# decorador original: @BWUtil.if_only_not_component(...)
def patch_future_builtins_open():
    ...
# decorador original: @BWUtil.if_only_not_component(...)
def set_threading_bootstrap():
    ...
def main():
    ...
