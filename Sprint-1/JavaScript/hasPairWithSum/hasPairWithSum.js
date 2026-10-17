/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity:
 * Space Complexity:
 * Optimal Time Complexity:
 * 
 * Time Complexity: O(N^2)
// Space Complexity: O(1)
// Optimal Time Complexity: O(N)
 *
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
export function hasPairWithSum(numbers, target) {
  const seenNumbers = new Set();

  for (const currentNumber of numbers) {
    const complement = target - currentNumber;

    if (seenNumbers.has(complement)) return true;

    seenNumbers.add(currentNumber);
  }
  return false;

}


// Time Complexity: O(n) We check each number once.
// Space Complexity: O(n) The Set may store all n numbers.