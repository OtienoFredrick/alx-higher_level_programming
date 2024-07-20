#!/usr/bin/node
const myVar = process.argv.slice(2);
const firstArg = myVar[0];

if (firstArg !== undefined)
{
	console.log(firstArg);
}else{
	console.log("No argument")
}
