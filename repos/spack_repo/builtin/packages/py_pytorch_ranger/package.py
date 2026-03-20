# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPytorchRanger(PythonPackage, CudaPackage):
    """
    Ranger - a synergistic optimizer using RAdam
    (Rectified Adam) and LookAhead in one codebase
    """

    homepage = "https://github.com/mpariente/Ranger-Deep-Learning-Optimizer"
    git = "https://github.com/mpariente/Ranger-Deep-Learning-Optimizer.git"
    pypi = "pytorch_ranger/pytorch_ranger-0.1.1.tar.gz"

    maintainers("LydDeb")

    license("Apache-2.0", checked_by="LydDeb")

    version("0.1.1", sha256="aa7115431cef11b57d7dd7bc86e7302a911dae467f62ec5d0b10e1ff744875db")

    with default_args(type="build"):
        depends_on("py-setuptools")

    with default_args(type=("build", "run")):
        depends_on("py-torch")
