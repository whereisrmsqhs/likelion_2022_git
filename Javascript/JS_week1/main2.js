let bool1 = true;
console.log(bool1);

let bool2 = 7 > 10;
console.log(bool2);

let arr = [10,20,"abc",true,null,undefined,function(){},{}];
console.log(arr);
console.log(arr[1]);

let obj = {koreanScore: 90, englishScore: 70, "math Score": 80};
console.log(obj["math Score"]);
console.log(obj.englishScore);

const gugudan = function gugudan(){
    console.log("3 * 1 = 3");
};

gugudan();
gugudan();

function printFruit(name,price){
    console.log(name+"is "+price+" won");
}

printFruit("banana",2000);
printFruit("apple",3000);

function sum(num1, num2){
    return num1 + num2;
}
const result = sum(10,20);
console.log(result);

