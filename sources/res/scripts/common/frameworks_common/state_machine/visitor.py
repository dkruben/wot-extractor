# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/frameworks_common/state_machine/visitor.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/frameworks_common/state_machine/visitor.py
from __future__ import absolute_import
import typing
from .transitions import BaseTransition
from .exceptions import NodeError
from .node import Node
if typing.TYPE_CHECKING:
    from . import State

def getAncestors(node, upper=None):
    if not isinstance(node, Node):
        raise NodeError(('Invalid argument "node" = {}').format(node))
    if upper is not None and not isinstance(upper, Node):
        raise NodeError(('Invalid argument "upper" = {}').format(upper))
    result = []
    found = node.getParent()
    while found != upper and found is not None:
        result.append(found)
        found = found.getParent()

    return result


def isDescendantOf(node, ancestor):
    if not isinstance(node, Node):
        raise NodeError(('Invalid argument "node" = {}').format(node))
    if not isinstance(ancestor, Node):
        raise NodeError(('Invalid argument "ancestor" = {}').format(ancestor))
    found = node.getParent()
    while found is not None:
        if found == ancestor:
            return True
        found = found.getParent()

    return False


def getDescendantIndex(node, ancestor, filter_=None):
    children = ancestor.getChildren(filter_=filter_)
    for index, child in enumerate(children):
        if child == node or isDescendantOf(node, child):
            return index

    return -1


def getLCA(nodes, upper=None):
    if not nodes:
        return
    else:
        ancestors = getAncestors(nodes[0], upper=upper)
        others = nodes[1:]
        others.reverse()
        while ancestors:
            ancestor = ancestors.pop(0)
            found = False
            for state in others:
                if isDescendantOf(state, ancestor):
                    found = True

            if found:
                return ancestor

        return


def getEffectiveTargetStates(transition, history):
    targets = []
    for state in transition.getTargets():
        if state.isHistory():
            stateID = state.getStateID()
            if stateID in history:
                targets.extend(history[stateID])
            else:
                defaultHistory = state.getTransitions()
                if defaultHistory:
                    targets.extend(getEffectiveTargetStates(defaultHistory[0], history))
        else:
            targets.append(state)

    return targets


def getTransitionDomain(transition, history, upper=None):
    states = getEffectiveTargetStates(transition, history)
    if states:
        return getLCA([transition.getSource()] + states, upper=upper)
    else:
        return
