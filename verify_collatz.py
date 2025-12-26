"""
Collatz Geometric Analysis - Computational Verification Tool

This script computes the Collatz parallelogram metrics for various N values
and verifies the geometric properties described in the research.

Author: Khan Sk Sohail
Email: ksksohail07@gmail.com
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def collatz_steps(n):
    """Compute stopping time for number n"""
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

def compute_parallelogram_data(N):
    """Compute all Collatz data up to limit N"""
    points = []
    max_steps = 0
    
    for n in range(1, N + 1):
        steps = collatz_steps(n)
        points.append((steps, n))
        if steps > max_steps:
            max_steps = steps
    
    return {
        'H': N,
        'W': max_steps,
        'points': points,
        'aspect_ratio': N / max_steps
    }

def linear_regression_angle(points):
    """Compute tilt angle from linear regression"""
    x = np.array([p[0] for p in points])  # steps
    y = np.array([p[1] for p in points])  # n
    
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    angle = np.arctan(slope) * 180 / np.pi
    
    return angle, r_value**2

def verify_data():
    """Verify the reported data"""
    limits = [500, 4000, 10000]
    
    print("Collatz Parallelogram Verification")
    print("=" * 60)
    print(f"{'N':<10} {'W':<10} {'H/W':<12} {'θ (deg)':<12} {'R²':<10}")
    print("-" * 60)
    
    for N in limits:
        print(f"Computing N={N}...", end=" ")
        data = compute_parallelogram_data(N)
        angle, r_squared = linear_regression_angle(data['points'])
        
        print(f"{N:<10} {data['W']:<10} {data['aspect_ratio']:<12.2f} "
              f"{angle:<12.2f} {r_squared:<10.4f}")
    
    print("=" * 60)

def plot_parallelogram(N=10000):
    """Visualize the Collatz parallelogram"""
    data = compute_parallelogram_data(N)
    points = data['points']
    
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    
    plt.figure(figsize=(12, 8))
    plt.scatter(x, y, alpha=0.5, s=1)
    plt.xlabel('Steps (Width)', fontsize=12)
    plt.ylabel('n (Height)', fontsize=12)
    plt.title(f'Collatz Parallelogram (N={N})', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f'collatz_parallelogram_N{N}.png', dpi=300)
    print(f"Saved visualization: collatz_parallelogram_N{N}.png")

if __name__ == "__main__":
    # Verify the data
    verify_data()
    
    # Create visualization
    print("\nGenerating visualization...")
    plot_parallelogram(10000)
    
    print("\nVerification complete!")
