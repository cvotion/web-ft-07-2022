
const string = '{}[{}]}';

// Option 1


function checkPair(string){
    
    strArr = string.split('');
    let stack = []
    
    for (let i = 0 ; i < strArr.length ; i ++){
        if (strArr[i] === '{' || strArr[i] === '[' || strArr[i] === '('){
            stack.push(strArr[i]);
            console.log(stack)
            continue;
        }
        if (stack.length === 0){
            return false;
        }
        else if (strArr[i] === '}'){
            if (stack.includes('{')){
                let index = stack.indexOf('{')
                stack.splice(index)
                console.log(stack)
            }
            else{
                return false
            }
        }
        else if (strArr[i] === ']'){
            if (stack.includes('[')){
                let index = stack.indexOf('[')
                stack.splice(index)
                console.log(stack)
            }
            else{
                return false
            }
        }
        else if (strArr[i] === ')'){
            if (stack.includes('(')){
                let index = stack.indexOf('(')
                stack.splice(index)
                console.log(stack)
            }
            else{
                return false
            }
        }
        
        
    }
    return true

}    

console.log(checkPair('{}[{}]{}}'))