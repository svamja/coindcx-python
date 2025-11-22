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
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Python wrapper for CoinDCX API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/coindcx-python",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    keywords="coindcx api trading cryptocurrency bitcoin ethereum",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/coindcx-python/issues",
        "Source": "https://github.com/yourusername/coindcx-python",
        "Documentation": "https://docs.coindcx.com",
    },
)
