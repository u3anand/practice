use std::time::Instant;

pub struct Solution;

impl Solution {
    pub fn plus_one(digits: Vec<i32>) -> Vec<i32> {
        let mut result = Vec::with_capacity(digits.len() + 1);
        let mut carry = 1;

        for &digit in digits.iter().rev() {
            let sum = digit + carry;
            result.push(sum % 10);
            carry = sum / 10;
        }

        if carry > 0 {
            result.push(carry);
        }

        result.reverse();
        result
    }
}

fn main() {
    let digits = vec![1, 2, 3];

    // Start timing
    let start = Instant::now();
    let result = Solution::plus_one(digits);
    let duration = start.elapsed();

    // Print result
    println!("{:?}", result);

    // Print execution time
    println!("Execution time: {:.6} ms", duration.as_secs_f64() * 1000.0);
}
