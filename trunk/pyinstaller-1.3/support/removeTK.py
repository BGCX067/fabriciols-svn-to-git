# Copyright (C) 2005, Giovanni Bajo
# Based on previous work under copyright (c) 2002 McMillan Enterprises, Inc.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA
import sys, os

def empty(dir):
    try:
        fnms = os.listdir(dir)
    except OSError:
        return
    for fnm in fnms:
        path = os.path.join(dir, fnm)
        if os.path.isdir(path):
            empty(path)
            try:
                os.rmdir(path)
            except:
                pass
        else:
            try:
                os.remove(path)
            except:
                pass

tcldir = os.environ['TCL_LIBRARY']
prvtdir = os.path.dirname(tcldir)
if os.path.basename(prvtdir) == '_MEI':
    empty(prvtdir)
    os.rmdir(prvtdir)

