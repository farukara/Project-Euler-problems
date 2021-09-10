//!javascript
/* coding: utf-8
https://projecteuler.net/problem=63 */

//22 and 10 is choosen to avoid getting into large number e notation problem. besides there is some math logic that i can not be larger that 10
let count = 0;
let limit = 22; 
for (let i=1; i < 10; i++) {
    for (let j=1; j < limit; j++) {
        if (Math.pow(i, j).toString().length == j) {
            console.log(Math.pow(i,j))
            count++;
        }
    }
}

console.log(count);
