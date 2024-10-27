/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let val;
    
    if (nums.length === 0) {
        console.log('helllo')
        return init}

    for (let i=0;i<nums.length;i++) {
        if (i === 0) {
            val = fn(init, nums[i]) 
        } if (i > 0) {
            val = fn(val, nums[i])
        } 
        
    }
    return val
    
};