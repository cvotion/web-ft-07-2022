let arr = [34, 22, 10, 19, 17]

for (let i = 0; i < arr.length; i ++){
    for (let x = 0; x < arr.length-1; x ++){
        if (arr[x+1] < arr[x]){
            [arr[x+1],arr[x]] = [arr[x], arr[x+1]];
        }
    }
    
}

console.log(arr)