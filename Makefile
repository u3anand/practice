CXX = g++
CXXFLAGS = -std=c++23 -Wall -Wextra -O2

# Format all code
.PHONY: format
format:
	@echo "Formatting Python files..."
	@uv run ruff format daily/ questions/ 2>/dev/null || echo "No Python files to format"
	@echo "Formatting Go files..."
	@gofmt -w daily/ questions/ 2>/dev/null || echo "No Go files to format"
	@echo "Formatting Rust files..."
	@find daily/ questions/ -name "*.rs" -exec rustfmt {} \; 2>/dev/null || echo "No Rust files to format"
	@echo "Formatting C++ files..."
	@find daily/ questions/ \( -name "*.cpp" -o -name "*.h" \) -exec clang-format -i {} \; 2>/dev/null || echo "Note: clang-format not installed, skipping C++"
	@echo "Done!"

# Test all solutions in a directory
.PHONY: test-all
test-all:
	@echo "Testing Python..."
	@uv run python solution.py || true
	@echo ""
	@echo "Testing Go..."
	@go run solution.go || true
	@echo ""
	@echo "Testing Rust..."
	@cargo run --quiet || true
	@echo ""
	@echo "Testing C++..."
	@$(CXX) $(CXXFLAGS) solution.cpp -o solution && ./solution || true
	@rm -f solution

# Python
.PHONY: python
python:
	uv run python solution.py

# Go
.PHONY: go
go:
	go run solution.go

# Rust
.PHONY: rust
rust:
	cargo run --quiet

# C++
.PHONY: cpp
cpp:
	$(CXX) $(CXXFLAGS) solution.cpp -o solution && ./solution

# Clean
.PHONY: clean
clean:
	@find . -type f \( -name "solution" -o -name "solution_rs" -o -name "*.o" -o -name "a.out" \) -delete
	@find . -type d -name "target" -exec rm -rf {} + 2>/dev/null || true
	@echo "Cleaned build artifacts"

