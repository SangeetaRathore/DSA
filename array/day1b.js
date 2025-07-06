const input = require("../input/readlineInput")
async function main() {
    //Write a JavaScript function to clone an array.
    
    let myInput = JSON.parse(await(input('Enter ')))
    let answer = myInput.slice()
    console.log( typeof answer);
    console.log(answer);
}

/*
The Array slice() method returns selected elements in an array as a new array. It selects from a given start, up to a (not inclusive) given end. This method does not change the original array, enabling non-destructive extraction of array segments. excliuding last element.
myArray.slice(start,end)

the slice() method extracts the entire array from the given string and returns it as the answer, Since no arguments were passed to it.
*/

main()