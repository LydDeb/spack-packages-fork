# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNumpoly(PythonPackage):
    """Polynomials as a numpy datatype"""

    homepage = "https://pypi.org/project/numpoly"
    pypi = "numpoly/numpoly-1.3.9.tar.gz"

    maintainers("LydDeb")

    license("BSD-2-Clause", checked_by="LydDeb")

    version("1.3.9", sha256="7724d8ff0ab5014c0704c92892ffd845cefc9e17a6cf4a06d9398e45502554fd")
    version("1.3.4", sha256="e124a592ad535ac56952c1ca7f90ecea25d5354a13a428920bf6ee3f878c36cc")

    depends_on("c", type="build")

    depends_on("python@3.9:", type=("build", "run"), when="@1.3.9:")
    depends_on("python@3.7:", type=("build", "run"), when="@1.3.4:")
    with default_args(type="build"):
        depends_on("py-setuptools@40.9.0:")
        depends_on("py-wheel")
        depends_on("py-cython")

    with default_args(type=("build", "run")):
        depends_on("py-numpy@2:", when="@1.3.9:")
        depends_on("py-numpy@1.20:", when="@1.3.4:")
        depends_on("py-importlib-metadata")
