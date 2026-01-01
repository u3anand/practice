package main

import (
	"fmt"
	"time"
)

// Solution represents the solution structure
type Solution struct{}

func (s *Solution) PlusOne(digits []int) []int {
	carry := 1
	result := make([]int, 0, len(digits)+1)

	for i := len(digits) - 1; i >= 0; i-- {
		sum := digits[i] + carry
		result = append([]int{sum % 10}, result...)
		carry = sum / 10
	}

	if carry > 0 {
		result = append([]int{carry}, result...)
	}

	return result
}

func main() {
	sol := &Solution{}
	digits := []int{1, 2, 3}

	// Start timing
	start := time.Now()
	result := sol.PlusOne(digits)
	duration := time.Since(start)

	// Print result
	fmt.Println(result)

	// Print execution time
	fmt.Printf("Execution time: %.6f ms\n", float64(duration.Nanoseconds())/1e6)
}
