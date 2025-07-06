const input = require ('../input/readlineInput')
async function main(){
    // Write a JavaScript function to get the first element of an array. Passing the parameter 'n' will return the first 'n' elements of the array.

    let myInput = JSON.parse(await(input()))
    let num = JSON.parse(await(input()))

    if (num == null) {
        console.log( myInput[0])
    }

 
    if (num < 0){
    console.log([]);
    
    }
    // let answer = 
    console.log(myInput.slice(0,num));
    
    
}

main()