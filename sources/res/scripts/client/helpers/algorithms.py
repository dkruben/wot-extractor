# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/helpers/algorithms.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/algorithms.py
from __future__ import absolute_import
import heapq, typing
if typing.TYPE_CHECKING:
    from typing import Dict, List, Tuple
T = typing.TypeVar('T')

def shortestPath(graph, start, end):
    pq = []
    heapq.heappush(pq, (0.0, start))
    distances = {node: float('inf') for node in graph}
    distances[start] = 0.0
    previous = {node: None for node in graph}
    while pq:
        currentDistance, currentNode = heapq.heappop(pq)
        if currentDistance > distances[currentNode]:
            continue
        for node, distance in graph[currentNode]:
            distance += currentDistance
            if distance < distances[node]:
                distances[node] = distance
                heapq.heappush(pq, (distance, node))
                previous[node] = currentNode

    path = []
    if previous[start] is not None and start != end:
        return path
    else:
        while end is not None:
            path.append(end)
            end = previous[end]

        return path[::-1]
