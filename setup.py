from setuptools import setup, find_packages

setup(
    name="lnkd",
    version="0.1.1.post1",
    description="A simple utility for linked YAML files.",
    author="Mark Douthwaite",
    author_email="mark.douthwaite@peak.ai",
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    install_requires=["requests", "pyyaml"],
    include_package_data=True,
)
