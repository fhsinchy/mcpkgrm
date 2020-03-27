import os.path
from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

# This call to setup() does all the work
setup(
    name="mcpkgrm",
    version="1.0.0",
    description="Uninstall macOS packages easily and for free",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/fhsinchy/mcpkgrm",
    author="macOS(mc) Package(pkg) Remove(rm)",
    author_email="mail@farhan.info",
    license="GPL-3.0",
    classifiers=[
        "License :: OSI Approved :: GPL-3.0 License",
        "Programming Language :: Python :: 3",
    ],
    packages=["mcpkgrm"],
    entry_points={"console_scripts": ["mcpkgrm=mcpkgrm.__main__:main"]},
)
