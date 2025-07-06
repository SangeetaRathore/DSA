const input = require("../input/readlineInput")

async function main() {
    // Write a JavaScript function to check whether an `input` is an array or not.
    const isArray = await(input('enter '))
    let answer = JSON.parse(isArray)
    if(Array.isArray(answer)){
        console.log(true);
    }
    else{
        console.log(false)
    }
    
    /* notes: 
    1. Readline reads all the input as string.
    2. JSON.parse() convert that string into a real JavaScript object, such as:
    Turns "[1, 2, 3]" → [1, 2, 3] → ✅ Now it's a real array.
    Turns "123" → 123
    Turns "\"hello\"" → "hello"
    Turns "true" → true
    */
 
}

main()