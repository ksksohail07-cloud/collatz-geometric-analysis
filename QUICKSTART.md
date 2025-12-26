# Quick Start Guide

Get started with Collatz Geometric Analysis in 5 minutes!

## 🚀 Installation

### Prerequisites
- Python 3.7+
- pip

### Install Dependencies
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install numpy scipy matplotlib
```

## 📊 Run Verification

### Basic Verification
```bash
python verify_collatz.py
```

This will:
- Compute W values for N=500, 4000, 10000
- Calculate aspect ratios and tilt angles
- Display results in a formatted table
- Generate visualization (saved as PNG)

### Expected Output
```
Collatz Parallelogram Verification
============================================================
N          W          H/W          θ (deg)      R²        
------------------------------------------------------------
Computing N=500... 500        143        3.49         74.01        0.9xxx
Computing N=4000... 4000       237        16.87        86.61        0.9xxx
Computing N=10000... 10000      261        38.31        88.50        0.9xxx
============================================================
```

## 🔍 Custom Analysis

### Compute for Different N
```python
from verify_collatz import compute_parallelogram_data

# Compute for N=50000
data = compute_parallelogram_data(50000)
print(f"N={data['H']}, W={data['W']}, Aspect Ratio={data['aspect_ratio']:.2f}")
```

### Generate Visualization
```python
from verify_collatz import plot_parallelogram

# Create visualization for N=20000
plot_parallelogram(20000)
```

## 📈 Analyze Results

### Check if W values match
Compare your computed W values with reported values:
- N=500: W should be 143
- N=4000: W should be 237
- N=10000: W should be 261

### Verify Logarithmic Growth
Plot log(W) vs log(N) to confirm linear relationship (slope ≈ 0.28)

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError"
**Solution:** Install missing dependencies
```bash
pip install -r requirements.txt
```

### Issue: Computation takes too long
**Solution:** Start with smaller N values
```python
# Test with N=1000 first
data = compute_parallelogram_data(1000)
```

### Issue: Different W values
**Solution:** Please report! Open an issue with:
- Your computed values
- Python version
- Operating system

## 📚 Next Steps

1. **Verify the data** - Run verification and compare results
2. **Explore visualizations** - Generate plots for different N
3. **Read the paper** - Check [Overleaf document](link)
4. **Contribute** - See [CONTRIBUTING.md](CONTRIBUTING.md)
5. **Ask questions** - See [FAQ.md](FAQ.md)

## 💡 Quick Examples

### Example 1: Single Number
```python
def collatz_steps(n):
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps

print(f"27 takes {collatz_steps(27)} steps")  # Output: 111 steps
```

### Example 2: Find Maximum
```python
def max_width(N):
    return max(collatz_steps(n) for n in range(1, N + 1))

print(f"Max width for N=1000: {max_width(1000)}")
```

### Example 3: Aspect Ratio
```python
N = 10000
W = max_width(N)
aspect_ratio = N / W
print(f"Aspect ratio: {aspect_ratio:.2f}")
```

## 🎯 Performance Tips

- **For N ≤ 10,000:** Runs in seconds
- **For N ≤ 100,000:** May take minutes
- **For N ≤ 1,000,000:** May take hours
- **For N > 1,000,000:** Consider optimization or parallel processing

## 📞 Get Help

- **Issues:** https://github.com/ksksohail07-cloud/collatz-geometric-analysis/issues
- **Email:** ksksohail07@gmail.com
- **FAQ:** [FAQ.md](FAQ.md)

---

**Ready to contribute?** See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines!