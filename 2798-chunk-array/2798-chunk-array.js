/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    let chunked_arr = []
   
    for (let i=0; i<arr.length/size; i++) {
        let subarr = []
        
        for (let j=(i*size); j<((i+1)*size); j++) {

            if (arr[j] == null) {
                break
            }

            subarr.push(arr[j])
            
        }
        chunked_arr.push(subarr)
    }
    return chunked_arr
    
};
