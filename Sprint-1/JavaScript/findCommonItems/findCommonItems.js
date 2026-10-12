/**
 * Finds common items between two arrays.
 *
 * Time Complexity:
 * Space Complexity:
 * Optimal Time Complexity:
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 * 
 * Time Complexity: O(n * m)
 * Space Complexity: O(u)
 * Optimal Time Complexity: O(n + m)
 */
export const findCommonItems = (firstArray, secondArray) => {
  const allowedItems = new Set(secondArray);

  const uniqueValues = [
    ...new Set(firstArray.filter((item) => allowedItems.has(item))),
  ];
  return uniqueValues;
};

console.log(findCommonItems([2, 5, 7], [5, 6, 7]));

// Time:O(n \ m)	filter() visits each item in the first array, and includes() may scan the second array each time.
// Sace: O(k)	The Set stores unique common items, and the resulting array contains those items.
// Optimal time: O(n+m) Achievable on average using a Set for efficient lookups.