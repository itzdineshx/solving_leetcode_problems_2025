/**
 * @param {number} n - The initial count value
 * @return {Function} counter - A function that increments and returns the current count
 */

/**
 * Approach:
 * - Create a function `createCounter` that takes an initial number `n` as input.
 * - Return an inner function that, when called, returns the current value of `n` and then increments it.
 */

var createCounter = function(n) {
    
    return function() {
        return n++;  // Return the current count and increment it for the next call
    };
};

/** 
 * Example usage:
 * const counter = createCounter(10);
 * console.log(counter()); // 10
 * console.log(counter()); // 11
 * console.log(counter()); // 12
 */

/**
 * Workflow:
 * 1. Call `createCounter(n)` with an initial value.
 * 2. Each call to the returned function returns the current value of `n`, then increments it.
 * 3. The value persists across function calls due to closure.
 *
 * Time Complexity: O(1) - Each call only performs a single increment operation.
 * Space Complexity: O(1) - Only one variable (`n`) is stored in memory.
 */
