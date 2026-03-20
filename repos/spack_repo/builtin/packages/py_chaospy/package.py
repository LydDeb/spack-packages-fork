# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyChaospy(PythonPackage):
    """Numerical tool for performing uncertainty quantification"""

    homepage = "https://github.com/jonathf/chaospy"
    git = "https://github.com/jonathf/chaospy.git"
    pypi = "chaospy/chaospy-4.3.21.tar.gz"

    maintainers("LydDeb")

    license("MIT", checked_by="LydDeb")

    version("4.3.21", sha256="a7ab9bd376c5e956a5f263d5b481a0a596e49954531698cc169f0711851d5ae3")

    depends_on("python@3.9:", type=("build", "run"))
    with default_args(type="build"):
        depends_on("py-setuptools@45:")

    with default_args(type=("build", "run")):
        depends_on("py-numpy@1.20:")
        depends_on("py-numpoly@1.2.12:")
        depends_on("py-scipy")
        depends_on("py-importlib-metadata", when="^python@:3.9")
