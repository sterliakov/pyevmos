[![PyPi Version](https://img.shields.io/pypi/v/evmos.svg)](https://pypi.python.org/pypi/evmos/)
[![Python Versions](https://img.shields.io/pypi/pyversions/evmos.svg)](https://pypi.python.org/pypi/evmos/)
[![Read the Docs](https://readthedocs.org/projects/pyevmos/badge/?version=latest)](https://pyevmos.readthedocs.io/en/latest/?badge=latest)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-blue-blue.svg)](https://blue.readthedocs.io/)
![](https://github.com/sterliakov/pyevmos/actions/workflows/test.yml/badge.svg)

# Pyevmos - Python SDK to assist developers on Evmos chain.

**Disclaimer: this package is not officialy maintained by Evmos affiliates.**
Read our [documentation](https://pyevmos.readthedocs.io/en/latest/index.html) on ReadTheDocs.

This project is a direct python port of [evmosjs](https://github.com/evmos/evmosjs) library.


# Installation

Install with pip:

```bash
pip install -U evmos
```

Install from source:

```bash
git clone https://github.com/sterliakov/pyevmos/
cd pyevmos
pip install .
```

Supported extras:

- `test`: install test dependencies (`pip install evmos[test]`)
- `dev`: install development dependencies (`pip install evmos[dev]`) - currently `pre-commit` and `compiler` extension for `betterproto`.
- `docs`: dependencies for building documentation (`pip install evmos[docs]`)
