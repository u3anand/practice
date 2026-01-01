#include <chrono>
#include <iomanip>
#include <iostream>
#include <vector>

using namespace std;
using namespace std::chrono;

class Solution {
public:
  vector<int> plusOne(vector<int> &digits) {
    vector<int> result;
    int carry = 1;

    for (int i = digits.size() - 1; i >= 0; --i) {
      int sum = digits[i] + carry;
      result.insert(result.begin(), sum % 10);
      carry = sum / 10;
    }

    if (carry > 0) {
      result.insert(result.begin(), carry);
    }

    return result;
  }
};

int main() {
  Solution sol;
  vector<int> digits = {1, 2, 3};

  // Start timing
  auto start = high_resolution_clock::now();
  vector<int> result = sol.plusOne(digits);
  auto end = high_resolution_clock::now();

  // Calculate duration
  auto duration = duration_cast<nanoseconds>(end - start);

  // Print result
  cout << "[";
  for (size_t i = 0; i < result.size(); ++i) {
    cout << result[i];
    if (i < result.size() - 1)
      cout << ", ";
  }
  cout << "]" << endl;

  // Print execution time
  cout << fixed << setprecision(6);
  cout << "Execution time: " << duration.count() / 1e6 << " ms" << endl;

  return 0;
}
