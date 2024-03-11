#!/usr/bin/node

const args = process.argv.slice(2);
if (args.length <= 1) {
  console.log(0);
} else {
  const numbers = args.map(Number);
  const max = Math.max(...numbers);
  const secondMax = numbers.filter(num => num < max).reduce((a, b) => Math.max(a, b), -Infinity);
  console.log(secondMax);
}
