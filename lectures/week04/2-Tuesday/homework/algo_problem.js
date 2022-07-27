var arr = [
    [3, 2],
    [1,1, 4, 6],
    [3, 4,2]];
let sums = [];
let sum = 0;
// Sort the array by the sum of each inner array.For the above example, the respective sums for each inner array is 5, 12, and 9. Therefore, the solution should be:
for (let a = 0 ; a < arr.length ; a ++){
    for (let b = 0; b < arr[a].length ; b ++){
        sum += arr[a][b];
    }
    sums.push([sum]);
    
}
for (let c = 0 ; c < sums.length ; c ++ ){
    for (let d = 0; d < sums.length-1 ; d ++){
    if(sums[d+1]>sums[d]){
        console.log(`[[${arr[d+1]}], [${arr[d]}]] = [[${arr[d]}], [${arr[d+1]}]]`);
        [arr[d+1], arr[d]] = [arr[d], arr[d+1]];
        [sums[d+1], sums[d]] = [sums[d], sums[d+1]];

        }
    }
}

console.log(arr)
// [[3,2],
// [3, 4,2]],
// [1,1, 4, 6]