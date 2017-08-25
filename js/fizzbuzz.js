// For colors, run 'npm install colors"

const colors = require('colors');

for (let num = 1; num <= 100; num++) {
    if (num % 3 === 0 && num % 5 === 0) {
        console.log(colors.blue('FizzBuzz'));
    } else if (num % 3 === 0) {
        console.log(colors.red('Fizz'));
    } else if (num % 5 === 0) {
        console.log(colors.yellow('Buzz'));
    } else {
        console.log(num);
    }
}
