"""Setup.py for a2j."""
import os

from setuptools import setup, find_packages

long_description = (os.path.dirname(os.path.realpath(__file__)) + os.sep + "README.md").read_text(encoding="utf-8")

with open("VERSION", "r") as file:
    version = file.read().strip()

setup(
    name="a2j",
    version=version,
    description="A JSON API analyzing Age of Empires II records.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Deasilsoft/a2j",
    author="Deasilsoft",
    author_email="business@deasilsoft.com",
    classifiers=[
        "Development Status :: 3 - Alpha",  # 3 = Alpha, 4 = Beta, 5 = Production/Stable
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    keywords="json, demo, parse, analyze, record, aoe2, aoe2record",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.9",
)
