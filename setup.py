from distutils.core import setup

import sys

if sys.version_info[0] < 3:
    raise Exception(
        "The jaxfenics only supports Python3. Did you run $python setup.py <option>.? Try running $python3 setup.py <option>."
    )

setup(
    name="jaxfenics",
    description="JAX-FEniCS interface",
    url="https://github.com/mansura-habiba/jax-fenics",
    author="Mansura Habiba",
    license="MIT",
    packages=["jaxfenics"],
    install_requires=["jax", "fenics", "fdm", "scipy"],
)
