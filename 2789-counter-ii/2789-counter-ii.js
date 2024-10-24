/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    n = init
    return {
        increment: function() {
            return n +=1
        },
        decrement: function() {
            return n -= 1
        },
        reset: function() {
            n = init
            return n
        }

    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */