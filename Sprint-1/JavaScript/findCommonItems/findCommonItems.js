/**
 * Finds common items between two arrays.
 * 
 * Time Complexity: O(n * m)
 * Space Complexity: O(n)
 * Optimal Time Complexity: O(n + m)
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
export const findCommonItems = (firstArray, secondArray) => {
  const allowedItems = new Set(secondArray);

  const uniqueValues = [
    ...new Set(firstArray.filter((item) => allowedItems.has(item))),
  ];
  return uniqueValues;
};

console.log(findCommonItems([2, 5, 7], [5, 6, 7]));


// Time Complexity: O(n + m) on average.
// Building the Set takes O(m), and filtering the first array takes O(n)
// on average because Set.has() provides efficient lookups.

// Space Complexity: O(n + m).
// The Set stores elements from secondArray, while the filter result
// and the Set of unique common items require additional space.

// Improvement: Reduces average time complexity from O(n * m) to O(n + m).