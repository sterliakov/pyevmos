[![PyPi Version](https://img.shields.io/pypi/v/evmos.svg)](https://pypi.python.org/pypi/evmos/)
[![Python Versions](https://img.shields.io/pypi/pyversions/evmos.svg)](https://pypi.python.org/pypi/evmos/)
[![Read the Docs](https://readthedocs.org/projects/pyevmos/badge/?version=latest)](https://pyevmos.readthedocs.io/en/latest/?badge=latest)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Linter: Ruff](https://img.shields.io/badge/Linter-Ruff-brightgreen?style=flat-square)](https://github.com/charliermarsh/ruff)
![](https://github.com/sterliakov/pyevmos/actions/workflows/test.yml/badge.svg)

# Maintenance note

Evmos v16 and later introduced several major changes to the upstream protocol.
This library is not actively maintained now due to insufficient demand - please
open an issue if you have interested in using pyevmos, I will be able to
allocate some time to it.

Version on master has several breaking changes and generates EIP-712
transactions that may be rejected by upstream nodes: "old-style" EIP-712
with `ExtensionOptionsWeb3Tx` are deprecated and no longer supported by recent
node versions. Currently master branch ships with protobuf files generated from
evmos `v20.0.0`.

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

- `dev`: install development dependencies (`pip install evmos[dev]`).
- `types`: install stubs for untyped dependencies.
