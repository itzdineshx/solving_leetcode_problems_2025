/**
 * @return {Function}
 */
var createHelloWorld = function() {
    
    return function(...args) {
        return "Hello World";
    }
};

/**
 * Example Usage:
 */
const f = createHelloWorld();
console.log(f());         // Output: "Hello World"
console.log(f(1, 2, 3));  // Output: "Hello World"
console.log(f("test"));   // Output: "Hello World"
