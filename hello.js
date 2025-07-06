const input = require("./input/readlineInput")
async function main() {
    // const name = await input("enter the name ")
    // console.log(name);

    const addNum1 = Number(await input('enter num 1 = '));
    const addNum2 = Number(await input ('enter num 2 = ')) 
    let add = addNum1+addNum2
    console.log(add);  
    
}

main()