const bubble_sort = (arr) => {
    for (let itr = 0; itr < arr.length; ++itr) {
        for (let cmp = 0; cmp < arr.length ; ++cmp)
        if (arr[cmp] > arr[cmp + 1]) {
                // console.log(i,j)
                
                let tmp = arr[cmp + 1];
                arr[cmp + 1] = arr[cmp];
                arr[cmp] = tmp;
            }
    }
    console.log(arr)
}

bubble_sort([3, 2, 1, 7, 5, 7,4,423543,354534,5435,435,3]);