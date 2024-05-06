
let a=10,b=20;

//Named Function
function add(x,y)
{
    console.log("add",x+y);
}
add(a,b);

//Anonymous Function
var adda=function(x,y){
    console.log("adda",x+y);
}
adda(a,b)

//Arrow Function
const greet=name=>"Hello "+name;
console.log(greet('Hey'));

const sq=x=>"Square of " +x +" is "+x*x;
console.log(sq(5));

//IIFE Function
(function(message){
    console.log(message)
})("This is by IIFE")

//Array Literals
const arr2=[1,2,3,4,5];
console.log(arr2);

//Array constructors
const arr3=new Array(1,2,3);
console.log(arr3);
const arr4=new Array(5);
console.log(arr4);

console.log(arr2.length)
console.log(arr2.push(6));
console.log(arr2.pop())
console.log(arr2.shift());
console.log(arr2);
console.log(arr2.unshift(0));
console.log(arr2);

arr2.splice(2,0,"hi","hello");;
console.log(arr2);

const num=[10,18,1,21,2];
console.log(num.sort());

var b1=num.sort(function(a,b){
    return a-b;
})
console.log(b1);