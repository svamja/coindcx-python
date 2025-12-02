"""
Setup configuration for coindcx package
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="coindcx",
    version="0.1.1",
    author="Sanjay Vamja",
    author_email="svamja@gmail.com",
    description="Python wrapper for CoinDCX API with support for spot, margin, and futures trading",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/svamja/coindcx-python",
    packages=find_packages(exclude=["tests", "examples", "ai", "venv"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Office/Business :: Financial",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    keywords="coindcx api trading cryptocurrency bitcoin ethereum futures spot margin",
    project_urls={
        "Bug Reports": "https://github.com/svamja/coindcx-python/issues",
        "Source": "https://github.com/svamja/coindcx-python",
        "Documentation": "https://github.com/svamja/coindcx-python#readme",
    },
    license="MIT",
)
