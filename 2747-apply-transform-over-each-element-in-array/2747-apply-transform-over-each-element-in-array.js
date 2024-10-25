/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    for (let i = 0; i < arr.length; i++) {
        if (fn.length === 1) {
            arr[i] = fn(arr[i])
        } else {
            arr[i] = fn(arr[i], i)
        }
    }
    return arr;
};
