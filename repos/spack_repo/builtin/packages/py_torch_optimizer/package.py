# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTorchOptimizer(PythonPackage, CudaPackage):
    """pytorch-optimizer"""

    homepage = "https://github.com/jettify/pytorch-optimizer"
    git = "https://github.com/jettify/pytorch-optimizer.git"
    pypi = "torch-optimizer/torch-optimizer-0.3.0.tar.gz"

    maintainers("LydDeb")

    license("Apachae-2.0", checked_by="LydDeb")

    version("0.3.0", sha256="b2180629df9d6cd7a2aeabe71fa4a872bba938e8e275965092568cd9931b924c")

    with default_args(type="build"):
        depends_on("py-setuptools")

    with default_args(type=("build", "run")):
        depends_on("py-torch@1.5.0:")
        depends_on("py-pytorch-ranger@0.1.1:")
