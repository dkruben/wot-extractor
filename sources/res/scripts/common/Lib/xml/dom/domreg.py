# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/xml/dom/domreg.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/xml/dom/domreg.py
from xml.dom.minicompat import *
import sys
well_known_implementations = {'minidom': 'xml.dom.minidom', 
   '4DOM': 'xml.dom.DOMImplementation'}
registered = {}

def registerDOMImplementation(name, factory):
    registered[name] = factory


def _good_enough(dom, features):
    for f, v in features:
        if not dom.hasFeature(f, v):
            return 0

    return 1


def getDOMImplementation(name=None, features=()):
    import os
    creator = None
    mod = well_known_implementations.get(name)
    if mod:
        mod = __import__(mod, {}, {}, ['getDOMImplementation'])
        return mod.getDOMImplementation()
    else:
        if name:
            return registered[name]()
        if not sys.flags.ignore_environment and 'PYTHON_DOM' in os.environ:
            return getDOMImplementation(name=os.environ['PYTHON_DOM'])
        if isinstance(features, StringTypes):
            features = _parse_feature_string(features)
        for creator in registered.values():
            dom = creator()
            if _good_enough(dom, features):
                return dom

        for creator in well_known_implementations.keys():
            try:
                dom = getDOMImplementation(name=creator)
            except StandardError:
                continue

            if _good_enough(dom, features):
                return dom

        raise ImportError, 'no suitable DOM implementation found'
        return


def _parse_feature_string(s):
    features = []
    parts = s.split()
    i = 0
    length = len(parts)
    while i < length:
        feature = parts[i]
        if feature[0] in '0123456789':
            raise ValueError, 'bad feature name: %r' % (feature,)
        i = i + 1
        version = None
        if i < length:
            v = parts[i]
            if v[0] in '0123456789':
                i = i + 1
                version = v
        features.append((feature, version))

    return tuple(features)
