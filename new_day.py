import sys
import os
from pathlib import Path
from datetime import datetime

PYTHON_TEMPLATE = '''#!/usr/bin/env python3
"""
Problem: [Problem Name]
"""

import time
from typing import List


class Solution:
    def solve(self, data):
        """Solve the problem."""
        # TODO: Implement solution
        pass


def main():
    # Test case
    data = None  # TODO: Add test input
    
    # Start timing
    start = time.perf_counter()
    result = Solution().solve(data)
    end = time.perf_counter()
    
    # Calculate duration in milliseconds
    duration_ms = (end - start) * 1000
    
    # Print result
    print(result)
    
    # Print execution time
    print(f"Execution time: {duration_ms:.6f} ms")


if __name__ == "__main__":
    main()
'''

CPP_TEMPLATE = '''#include <chrono>
#include <iomanip>
#include <iostream>
#include <vector>

using namespace std;
using namespace std::chrono;

class Solution {
public:
  /**
   * Solve the problem
   */
  void solve() {
    // TODO: Implement solution
  }
};

int main() {
  Solution sol;
  
  // Start timing
  auto start = high_resolution_clock::now();
  sol.solve();
  auto end = high_resolution_clock::now();
  
  // Calculate duration
  auto duration = duration_cast<nanoseconds>(end - start);
  
  // Print result
  // TODO: Print your result
  
  // Print execution time
  cout << fixed << setprecision(6);
  cout << "Execution time: " << duration.count() / 1e6 << " ms" << endl;
  
  return 0;
}
'''

GO_TEMPLATE = '''package main

import (
	"fmt"
	"time"
)

// Solution represents the solution structure
type Solution struct{}

// Solve solves the problem
func (s *Solution) Solve() {
	// TODO: Implement solution
}

func main() {
	sol := &Solution{}
	
	// Start timing
	start := time.Now()
	sol.Solve()
	duration := time.Since(start)
	
	// Print result
	// TODO: Print your result
	
	// Print execution time
	fmt.Printf("Execution time: %.6f ms\\n", float64(duration.Nanoseconds())/1e6)
}
'''

RUST_TEMPLATE = '''use std::time::Instant;

pub struct Solution;

impl Solution {
    /// Solve the problem
    pub fn solve() {
        // TODO: Implement solution
    }
}

fn main() {
    // Start timing
    let start = Instant::now();
    Solution::solve();
    let duration = start.elapsed();
    
    // Print result
    // TODO: Print your result
    
    // Print execution time
    println!("Execution time: {:.6} ms", duration.as_secs_f64() * 1000.0);
}
'''

def create_day(date_str=None):
    if date_str is None:
        date_str = datetime.now().strftime("%b%d").lower()
    
    day_dir = Path(__file__).parent / "daily" / date_str
    day_dir.mkdir(parents=True, exist_ok=True)
    
    # Create template files
    (day_dir / "question.txt").touch()
    (day_dir / "solution.py").write_text(PYTHON_TEMPLATE)
    (day_dir / "solution.cpp").write_text(CPP_TEMPLATE)
    (day_dir / "solution.go").write_text(GO_TEMPLATE)
    (day_dir / "solution.rs").write_text(RUST_TEMPLATE)
    
    # Create Cargo.toml
    cargo_toml = day_dir / "Cargo.toml"
    cargo_toml.write_text(f"""[package]
name = "{date_str}"
version = "0.1.0"
edition = "2021"

[[bin]]
name = "solution"
path = "solution.rs"
""")
    
    # Create go.mod
    go_mod = day_dir / "go.mod"
    go_mod.write_text(f"""module daily/{date_str}

go 1.23
""")
    
    # Update go.work
    go_work = Path(__file__).parent / "go.work"
    if go_work.exists():
        content = go_work.read_text()
        use_line = f"    ./daily/{date_str}\n"
        if use_line not in content:
            content = content.rstrip() + f"\n    ./daily/{date_str}\n"
            go_work.write_text(content)
    
    print(f"✅ Created daily/{date_str}/")
    print(f"   - All solution files with profiling")
    print(f"   - question.txt for problem description")
    print(f"\nRun with:")
    print(f"   Python: python solution.py")
    print(f"   C++:    g++ solution.cpp -o solution -O3 && ./solution")
    print(f"   Go:     go run solution.go")
    print(f"   Rust:   cargo run --release")

if __name__ == "__main__":
    date = sys.argv[1] if len(sys.argv) > 1 else None
    create_day(date)

