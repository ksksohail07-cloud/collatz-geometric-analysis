#!/bin/bash
# Quick Start Script for Collatz Research
# Author: Sahil Khan
# Date: December 30, 2025

echo "=================================="
echo "COLLATZ RESEARCH - QUICK START"
echo "=================================="
echo ""

# Check Python version
echo "Checking Python version..."
python3 --version || python --version

echo ""
echo "=================================="
echo "STEP 1: Install Dependencies"
echo "=================================="
pip install -r requirements.txt

echo ""
echo "=================================="
echo "STEP 2: Run Basic Verification"
echo "=================================="
echo "This will verify N=500, 4000, 10000"
echo ""
python3 verify_collatz.py || python verify_collatz.py

echo ""
echo "=================================="
echo "STEP 3: Run Extended Analysis"
echo "=================================="
echo "This will compute 8 data points"
echo "Expected time: 5-10 minutes"
echo ""
read -p "Press Enter to continue or Ctrl+C to skip..."
python3 extended_analysis.py || python extended_analysis.py

echo ""
echo "=================================="
echo "STEP 4: Run Advanced Verification"
echo "=================================="
echo "⚠️  WARNING: This will take several hours!"
echo "It will compute 13 data points up to N=1,000,000"
echo ""
read -p "Are you sure you want to continue? (y/n) " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]
then
    echo "Starting million-scale verification..."
    echo "You can monitor progress in real-time."
    echo "Results will be saved to:"
    echo "  - verification_results.json"
    echo "  - publication_quality_analysis.png"
    echo ""
    python3 advanced_verification.py || python advanced_verification.py
fi

echo ""
echo "=================================="
echo "EXECUTION COMPLETE!"
echo "=================================="
echo ""
echo "Next steps:"
echo "1. Review verification_results.json"
echo "2. Check publication_quality_analysis.png"
echo "3. Update DATA.md with findings"
echo "4. Follow PHD_RESEARCH_ROADMAP.md"
echo ""
echo "Repository: https://github.com/ksksohail07-cloud/collatz-geometric-analysis"
echo ""
