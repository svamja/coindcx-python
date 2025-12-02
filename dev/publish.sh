#!/bin/bash

# publish.sh - Build and publish package to PyPI
# This script cleans previous builds, creates new distribution packages,
# and publishes them to PyPI using twine.

set -e  # Exit on any error

echo "========================================"
echo "CoinDCX Package Publisher"
echo "========================================"
echo ""

# Navigate to project root (parent of dev directory)
cd "$(dirname "$0")/.."

# Check/install required tools
echo "🔧 Checking required tools..."
python3 -m pip install --upgrade pip build twine --quiet
echo "✓ Tools ready"
echo ""

# Clean previous builds
echo "🧹 Cleaning previous builds..."
rm -rf build/
rm -rf dist/
rm -rf *.egg-info
rm -rf coindcx.egg-info
echo "✓ Clean complete"
echo ""

# Build source distribution and wheel
echo "📦 Building package..."
python3 -m build
echo "✓ Build complete"
echo ""

# Check the distribution
echo "🔍 Checking package with twine..."
twine check dist/*
echo "✓ Check complete"
echo ""

# Upload to PyPI
echo "🚀 Publishing to PyPI..."
echo "You will be prompted for your PyPI credentials."
echo ""
twine upload dist/*

echo ""
echo "========================================"
echo "✓ Package published successfully!"
echo "========================================"
echo ""
echo "To install the latest version:"
echo "  pip install --upgrade coindcx"
echo ""
