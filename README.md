<h1 align="center">LNKD</h1>
<p align="center">Simple linked YAML documents.</p>

<p align="center">
<a href="https://github.com/markdouthwaite/lnkd/actions"><img alt="Build Status" src="https://github.com/markdouthwaite/lnkd/workflows/Build/badge.svg"></a>
<a href="https://github.com/pre-commit/pre-commit"><img alt="Uses pre-commit" src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white"></a>
<a href="https://github.com/ambv/black"><img alt="Code style: black" src="https://img.shields.io/badge/Code%20Style-black-000000.svg"></a>
</p>

A simple utility for linking YAML documents. For Python >=3.6.

## Getting started

You can install `lnkd` with:

```bash
pip install lnkd
```

## Why does it exist?

If you work with cloud technologies, YAML is part of your day job. It's often great for
managing complex service configurations, but it's also not uncommon to get YAML files
many hundreds of lines long. Some of the more advanced features of YAML -- such as
[merge tags](https://yaml.org/type/merge.html) make this process a little easier,but
not always ideal.

Long story short, this little package is the offshoot of an afternoon roaming the
interwebs trying to figure out how best to link YAML files across multiple local and
remote locations and stitch them together nicely. It is not the only way of doing this,
and it's also almost certainly not the best way of doing it. In fact, it will make it
very easy to create a lot of anti-patterns, and by default your YAML parser is unlikely
to get on well with the new tag. Adding new syntax is dangerous. You've been warned.

Anyway, it's here on the off-chance someone wants to avoid an afternoon of trawling
Stack Overflow.

Right, so how does it look?

You now get the `!@` tag to add to your YAML. Here's how it works:

Say we've a big ol' config file. Here we'll pretend it's a `docker-compose` file:

```yaml
# service.yaml
version: '3'
services:
    client:
        !@ client.yaml
```

And we store our `client` service config in a file `client.yaml`:

```yaml
# client.yaml
build:
    image: python:3.6-alpine
    environment:
        POSTGRES_USER: admin
        POSTGRES_PASSWORD: 1234
        POSTGRES_DB: accounts
```

If we then run:

```bash
lnkd service.yaml --output docker-compose.yaml
```

We'd get:


```yaml
# docker-compose.yaml
version: '3'
services:
    client:
        build:
            image: python:3.6-alpine
            environment:
              POSTGRES_USER: admin
              POSTGRES_PASSWORD: 1234
              POSTGRES_DB: accounts
```

And that's pretty much it. You can use these components programmatically to load and
build your YAML structures too.

# Notes

- If you can, use `anchors` and `aliases` instead. If you haven't heard of these before, Atlassian have written a [short example](https://confluence.atlassian.com/bitbucket/yaml-anchors-960154027.html).
- This package implements only custom tags. It _does not_ enable shared anchors and aliases across files.
