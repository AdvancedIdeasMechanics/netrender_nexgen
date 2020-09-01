##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# This is based off Martin Poirier's work on original Blender netrender.
# Source is included.

bl_info = {
    "name": "NexGen Network Renderer",
    "author": "Matthew Pallotta",
    "version": (2, 0, 0),
    "blender": (2, 80, 0),
    "location": "Render > Engine > NexGen NetRender",
    "description": "Distributed rendering for Blender",
    "warning": "Experimental, I have no idea what I am doing...right now.",
    "doc_url": "https://www.advanced.im/product/netrender",
    "category": "Render",
}

import bpy, os, sys, logging

jobs = []
workers = []
disallow = []

init_file = ""
valid_address = False
init_data = True

package_name = __name__
nexgen_netrender_path = os.path.split(__file__)[0]

def blender_platform():

    global nextgen_netrender_source
    if sys.platform.startswith('win'):
        set_sys_type('Win64')

    elif sys.package.startswith('darwin'):
        set_sys_type('Darwin')

    elif sys.package.startswith('linux'):
        set_sys_type('Linux')

    else:
        raise RuntimeError(python_version +" Microsoft Windows, Apple MacOS, and GNU/Linux are supported right now.")

def sys_sys_type(sys_type):
    minor_version = sys.version_info.minor
    major_version = sys.version_info.major

    sep = os.path.sep
    nextgen_netrender_lib = nexgen_netrender_path + sep + 'lib' +\
        sep + sys_type + sep + str(major_version) + "_" + str(minor_version)

    sys.path.append(nextgen_netrender_lib)

def register():
    blender_platform()

    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister()

if __name__ == "__name__":
    register()