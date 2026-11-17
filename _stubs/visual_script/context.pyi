# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/visual_script/context.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from inspect import ismethod as ismethod, getmembers as getmembers, getmro as getmro
from functools import wraps as wraps
from future.utils import lzip as lzip
from types import FunctionType as FunctionType
from typing import Tuple as Tuple, Callable as Callable, Sequence as Sequence
from constants import IS_DEVELOPMENT as IS_DEVELOPMENT, IS_PROCESS_REPLAY as IS_PROCESS_REPLAY
from py2to3.backport.inspect import getargspec as getargspec
from soft_exception import SoftException as SoftException
from visual_script.misc import ASPECT as ASPECT
from visual_script.debug_plan_loader import debugPlanLoader as debugPlanLoader

class UnsupportedMemberException(SoftException):
    func_name: Any
    aspect: Any
    def __init__(self, func_name, aspect):
        ...
    def __str__(self):
        ...

class MetaData(object):
    FUNC_CALL = 0
    EVENT_OUT = 1
    PROPERTY_GET = 2
    PROPERTY_SET = 3
    PROPERTY_PARAM_GET = 4
    UNDEFINED_SLOT_TYPE = 'Undefined'
    field: Any
    name: Any
    args: Any
    abstract: Any
    display_name: Any
    display_group: Any
    description: Any
    aspects: Any
    def __init__(self, field, name, args, **kwargs):
        ...
    def __repr__(self):
        ...
    @staticmethod
    def make_res_record(res_type):
        ...

class DispatchersHolder(object):
    ...

class VScriptContext(object):
    __active_vse_aspect: Any
    _vse_dispatchers: Any
    def __init__(self, aspect):
        ...
    def __del__(self):
        ...
    def destroy(self):
        ...
    def triggerEvent(self, name, *args):
        ...
    @property
    def _vse_aspect(self):
        ...
    @classmethod
    def _is_sub_class_of(cls, cls_name):
        ...

def vse_get_property(*args, **kwargs):
    ...
def vse_get_param_property(res, args, **kwargs):
    ...
def vse_set_property(*args, **kwargs):
    ...
def vse_func_call(res, args, **kwargs):
    ...
def vse_event_out(*args, **kwargs):
    ...
def vse_forward_event(name, argsSpecs, **kwargs):
    ...
def vse_context_effect_forward_event(name, argsSpecs, **kwargs):
    ...
