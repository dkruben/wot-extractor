# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/validate_shells.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/validate_shells.py
from __future__ import absolute_import, print_function
import ResMgr

def gatherChunks(spaceDir):
    if spaceDir[-1] != '/':
        spaceDir = spaceDir + '/'
    result = []
    entries = ResMgr.openSection(spaceDir)
    if entries:
        for entry in entries.keys():
            if entry[0] == '.':
                continue
            if ResMgr.isDir(spaceDir + entry):
                children = gatherChunks(spaceDir + entry)
                result.extend(children)
            else:
                entry = entry.lower()
                if len(entry) == 15 and entry[-6:] == '.chunk':
                    result.append(spaceDir + entry)

    return result


def validateShells(spaceDir):
    if spaceDir[-1] != '/':
        spaceDir = spaceDir + '/'
    chunks = gatherChunks(spaceDir)
    shells = [x for x in chunks if x[-7] == 'i']
    outsides = [x for x in chunks if x[-7] == 'o']
    for chunk in outsides:
        section = ResMgr.openSection(chunk)
        overlappers = section.readStrings('overlapper')
        for overlapper in overlappers:
            shell = spaceDir + overlapper + '.chunk'
            if shell in shells:
                shells.remove(shell)

    print(shells)
