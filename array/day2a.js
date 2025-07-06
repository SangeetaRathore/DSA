let input = require('../input/readlineInput')
async function main(){
    // Write a simple JavaScript program to join all elements of the following array into a string.

    let myinput = JSON.parse(await(input()));
    let answer1 = myinput.toString()
    console.log(answer1);
    console.log( typeof answer1);

    let answer2 = myinput.join()
    let answer3 = myinput.join('@')
    console.log(answer2);
    console.log(answer3);
    
    
    



    /* 
    We are using 2 methods that is toString() and join():
    In JavaScript, both the toString() and join() methods are used to convert elements of an array into a string. However, they differ in their flexibility and default behavior.
    1. toString() Method:
        The toString() method is a built-in method available on all JavaScript objects, including arrays.
        When called on an array, it converts the array elements into a single string. 
        By default, it uses a comma (,) as the separator between the array elements in the resulting string.
        It does not allow for specifying a custom separator.


    2. join() Method:
        The join() method is specifically designed for arrays.
        It also converts the array elements into a single string.
        The key difference is that it allows you to specify a custom separator to be used between the array elements.
        If no separator is provided, it defaults to using a comma (,), similar to toString().
     */
}

main()