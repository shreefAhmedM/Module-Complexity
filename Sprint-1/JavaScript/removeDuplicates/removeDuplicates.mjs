/**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
 *
 * Time Complexity:
 * Space Complexity:
 * Optimal Time Complexity:
 *
 * @param {Array} inputSequence - Sequence to remove duplicates from
 * @returns {Array} New sequence with duplicates removed
 */
export function removeDuplicates(inputSequence) {

  return [...new Set(inputSequence)]

}
// Original complexity:
// The original approach typically uses nested loops to compare
// each value with the remaining values in the sequence.
// This results in O(n²) time complexity because each value
// may be compared with every other value.


// Refactor:
// Use a Set to remove duplicate values while preserving the
// order of their first occurrence.
// The Set stores only unique values, and spreading the Set
// into a new array creates the result.
// Set insertion is O(1) on average, so processing all n
// elements takes O(n) time overall.