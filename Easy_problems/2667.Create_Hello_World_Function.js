/**
 * @return {Function} - A function that always returns "Hello World"
 */

/**
 * Approach:
 * - Create a function `createHelloWorld` that returns an inner function.
 * - The inner function takes any number of arguments (`...args`) but always returns "Hello World".
 */

var createHelloWorld = function() {
    
    return function(...args) {
        return "Hello World";  // Always return the fixed string
    };
};

/**
 * Example Usage:
 */
const f = createHelloWorld();
console.log(f());         // Output: "Hello World"
console.log(f(1, 2, 3));  // Output: "Hello World"
console.log(f("test"));   // Output: "Hello World"

/**
 * Workflow:
 * 1. Call `createHelloWorld()`, which returns a function.
 * 2. Invoke the returned function with or without arguments.
 * 3. The function ignores the arguments and returns "Hello World".
 *
 * Time Complexity: O(1) - The function always performs a single operation.
 * Space Complexity: O(1) - No additional data structures are used.
 */
