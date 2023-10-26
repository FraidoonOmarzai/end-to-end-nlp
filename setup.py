import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.1"

SRC_REPO = "textSummarizer"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
