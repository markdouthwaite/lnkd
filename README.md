<h1 align="center">LNKD</h1>
<p align="center">Simple linked YAML documents.</p>

<p align="center">
<a href="https://github.com/markdouthwaite/lnkd/actions"><img alt="Build Status" src="https://github.com/markdouthwaite/lnkd/workflows/Build/badge.svg"></a>
<a href="https://github.com/pre-commit/pre-commit"><img alt="Uses pre-commit" src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white"></a>
<a href="https://github.com/ambv/black"><img alt="Code style: black" src="https://img.shields.io/badge/Code%20Style-black-000000.svg"></a>
</p>

A template for Python packages. It does what it says on the tin. For Python >=3.6.

## Example

```yaml
# bob.yaml
name: bob
age: 42

```

```yaml
# person.yaml
version: '1'
person:
    !@ bob.yaml
    status: available
```

```python
import lnkd
import yaml

with open("spec.yaml") as target:
    yaml.load(target, Loader=lnkd.LinkedLoader)
```

```yaml
version: '1'
person:
    name: bob
    age: 42
    status: available
```

# Notes

- This package implements only custom tags. It _does not_ enable shared anchors and aliases across files.
