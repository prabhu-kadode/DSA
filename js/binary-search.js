function searchItem(nums,target){
    left = 0
    right = nums.length-1

    while (left<=right){
        mid = Math.floor((left+right)/2)

        if (nums[mid]===target){
            return true
        }
        if (nums[mid]<target){
            left = mid+1
        } else{
            right = mid-1
        }
    }
    return false
}

console.log(searchItem([1,2,3,4,5,6,7,8,9],9))