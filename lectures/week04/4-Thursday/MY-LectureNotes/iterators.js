
let arr = [45, 6, 7, 23, 33]

Array.prototype.myFilter = function(callBackFunction){
    let arr = []
    for(let i = 0 ; i < this.length ; i ++){
        let result = callBackFunction(this[i])
        if (result == true){
            arr.push(this[i])
        }
       
    }
    return arr
}

let result = arr.myFilter(num => num >15)

console.log(result);

Array.prototype.mySome = function(callBack){
    for (let i = 0 ; i < this.length ; i++){
        let result = callBack(this[i])
        if (result == true){
            return true
        }
        else{
            return false
        }
    }
}

let r = arr.mySome(num => num ==24)

console.log(r);