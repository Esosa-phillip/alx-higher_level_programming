#!/usr/bin/node
const Args = process.argv[2];
if (isNaN(Args)) {
  console.log('Not a number');
} else {
  console.log('My Number : ' + Args);
}
