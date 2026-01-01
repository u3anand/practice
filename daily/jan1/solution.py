#!/usr/bin/env python3
"""
Plus One - LeetCode Problem
Given a large integer represented as an array of digits, increment it by one.
"""

import time
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        result = []

        for i in range(len(digits) - 1, -1, -1):
            total = digits[i] + carry
            result.append(total % 10)
            carry = total // 10

        if carry:
            result.append(carry)

        return result[::-1]

def main():
    digits = [1, 2, 3]
    
    # Start timing
    start = time.perf_counter()
    result = Solution().plusOne(digits)
    end = time.perf_counter()
    
    # Calculate duration in milliseconds
    duration_ms = (end - start) * 1000
    
    # Print result
    print(result)
    
    # Print execution time
    print(f"Execution time: {duration_ms:.6f} ms")

if __name__ == "__main__":
    main()
