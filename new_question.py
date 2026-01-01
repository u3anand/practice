#!/usr/bin/env python3
"""
Script to create a new practice question/day with template files.
"""

import sys
import os
from pathlib import Path
from datetime import datetime


# Template files content
TEMPLATES = {
    "question.txt": """Problem: [Add problem title here]

Description:
[Add problem description here]

Examples:
Input: 
Output: 

Constraints:
[Add constraints here]
""",
    "solution.py": '''#!/usr/bin/env python3
"""
[Problem Name]
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
''',
    "solution.go": '''package main

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
''',
    "solution.rs": '''use std::time::Instant;

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
''',
    "solution.cpp": '''#include <chrono>
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
''',
    "Cargo.toml": """[package]
name = "{name}"
version = "0.1.0"
edition = "2021"

[[bin]]
name = "solution"
path = "solution.rs"
""",
    "go.mod": """module {folder}/{name}

go 1.23
""",
}


def create_question(folder: str, name: str):
    """Create a new question directory with template files.
    
    Args:
        folder: Either 'daily' or 'questions'
        name: Name of the question (e.g., 'jan1' or 'two-sum')
    """
    base_dir = Path(__file__).parent
    question_dir = base_dir / folder / name
    
    # Create directory
    question_dir.mkdir(parents=True, exist_ok=True)
    print(f"📁 Created directory: {folder}/{name}/")
    
    # Create template files
    for filename, content in TEMPLATES.items():
        filepath = question_dir / filename
        
        # Handle special cases for Cargo.toml and go.mod
        if filename == "Cargo.toml":
            content = content.format(name=name)
        elif filename == "go.mod":
            content = content.format(folder=folder, name=name)
        
        filepath.write_text(content)
        print(f"  ✓ {filename}")
    
    # Update go.work if needed
    go_work = base_dir / "go.work"
    if go_work.exists():
        content = go_work.read_text()
        use_line = f"    ./{folder}/{name}\n"
        if use_line not in content:
            content = content.rstrip() + f"\n    ./{folder}/{name}\n"
            go_work.write_text(content)
            print(f"  ✓ Updated go.work")
    
    print(f"\n✅ Created {folder}/{name}/ with all template files!")
    print(f"\nNext steps:")
    print(f"  1. cd {folder}/{name}")
    print(f"  2. Edit question.txt with problem description")
    print(f"  3. Implement solutions in solution.* files")
    print(f"\nRun with:")
    print(f"  Python: python solution.py")
    print(f"  C++:    g++ solution.cpp -o solution -O3 && ./solution")
    print(f"  Go:     go run solution.go")
    print(f"  Rust:   cargo run --release")


def main():
    if len(sys.argv) < 2:
        print("Usage: python new_question.py <name> [folder]")
        print("  name:   Question name (e.g., 'jan1', 'two-sum')")
        print("  folder: 'daily' or 'questions' (default: 'daily')")
        print("\nExamples:")
        print("  python new_question.py jan2")
        print("  python new_question.py two-sum questions")
        sys.exit(1)
    
    name = sys.argv[1]
    folder = sys.argv[2] if len(sys.argv) > 2 else "daily"
    
    if folder not in ["daily", "questions"]:
        print("❌ Folder must be 'daily' or 'questions'")
        sys.exit(1)
    
    create_question(folder, name)


if __name__ == "__main__":
    main()

