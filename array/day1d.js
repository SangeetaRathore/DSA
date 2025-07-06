const input = require ('../input/readlineInput')
async function main(){
    // Write a JavaScript function to get the last element of an array. Passing the parameter 'n' will return the last 'n' elements of the array.

    let myInput = JSON.parse(await(input()))
    let n = Number(await(input()))
    if (n==null){
        console.log(myInput); 
    }
    let answer = myInput.slice(Math.max(myInput.length-n,0)); 
    console.log(answer);
    
    
}

main()