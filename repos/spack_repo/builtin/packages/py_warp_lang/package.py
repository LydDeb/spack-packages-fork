# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyWarpLang(PythonPackage):
    """A Python framework for high-performance simulation and graphics programming"""

    homepage = "https://developer.nvidia.com/warp-python"

    url = "https://github.com/NVIDIA/warp/archive/refs/tags/v1.12.0.tar.gz"

    maintainers("LydDeb")

    license("Apache-2.0", checked_by="LydDeb")

    version("1.12.0", sha256="c5d2628781a2376e8a6e7d7bb169753b0e2537a31d78f2f1a6800498bfb0c1c8")

    depends_on("cxx", type="build")

    depends_on("python@3.9:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-setuptools@75.3.2:")
        depends_on("py-wheel")
        depends_on("py-build")

    with default_args(type=("build", "run")):
        depends_on("py-numpy")

    phases = ["build", "install"]

    def build(self, spec, prefix):
        python = spec["python"].command
        python("build_lib.py")
