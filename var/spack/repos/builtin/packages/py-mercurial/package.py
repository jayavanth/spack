##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class PyMercurial(Package):
    """Mercurial is a free, distributed source control management tool.
    It efficiently handles projects of any size and offers an easy and
    intuitive interface."""

    homepage = "https://www.mercurial-scm.org/"
    url = "https://pypi.python.org/packages/source/m/mercurial/mercurial-3.9.tar.gz"

    version('3.9', 'e2b355da744e94747daae3a5339d28a0',
            url="https://pypi.python.org/packages/22/73/e8ef24d3cb13e4fa2695417e13fd22effa1c8e28465eea91a9f84aa922cd/mercurial-3.9.tar.gz")

    extends('python')

    depends_on('py-setuptools', type='build')

    def install(self, spec, prefix):
        setup_py('install', '--prefix={0}'.format(prefix))