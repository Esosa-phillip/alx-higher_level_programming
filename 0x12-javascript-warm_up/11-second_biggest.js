#!/usr/bin/node
if (process.argv.length <= 3) console(0);
else {
  const args = process.argv.map(Number).slice(2, process.argv.length).sort((a, b) => b - a);
  console.log(args[1]);
}
