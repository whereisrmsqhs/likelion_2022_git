const sum = (num1, num2) => {
    return num1 + num2;
}

const pow = x => x * x;
console.log(pow);

const outer = (x) => () => x * x;

let remainder = 10 % 3;
console.log(remainder);

let hello = "hello," + "TTLSDF";
console.log(hello);

let str1 = `adadsasdasd asd as asd 'asd' asd' asd '`;
console.log(str1);

let name1 = 'mike';
let name2 = 'alice';

let string = `${name1} likes ${name2}`;
console.log(string);

///////////////////////////////

// === compare data type as well
let comparison2 = 10 === "10";
console.log(comparison2);

if(10 < 20){
    console.log("yeeeee~");
}
else if(30 < 20){
    console.log('30 is smaller than 20');
}
else{
    console.log("20 is larget than 10");
}

let animal = 'Dog';
switch(animal){
    case 'Cat':
        console.log('cat');
        break;
    case 'Dog':
        console.log('dog');
        break;
    default:
        console.log('Nothing');
        break;
}

let i=1;
while(i<10){
    console.log(i);
    i = i+1;
}

let flag = false;
do{
    console.log('do-while');
}while(flag === true);