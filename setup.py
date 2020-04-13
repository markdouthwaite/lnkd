from setuptools import setup, find_packages

setup(
    name="lnkd",
    version="0.1.2",
    description="A simple utility for linked YAML files.",
    author="Mark Douthwaite",
    author_email="mark@douthwaite.io",
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    install_requires=["requests", "pyyaml", "fire"],
    include_package_data=True,
    scripts=["bin/lnkd"],
)
