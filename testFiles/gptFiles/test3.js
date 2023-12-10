// No semicolon at the end of the line
const variable1 = "Hello";

// Incorrect indentation
if (true) {
  const wrongIndentation = "Indented incorrectly";
  console.log(wrongIndentation);
}

// Object injection (if the security/detect-object-injection rule checks for it)
const user = { name: "John" };
const userInput = getUserInput();
console.log(user[userInput]);

// Use of a magic number
const magicNumber = 42;

// Using deprecated API (if the node/no-deprecated-api rule checks for it)
const fs = require("fs");
fs.exists("/path", (exists) => {
  if (exists) {
    console.log("File exists");
  }
});

// Use of alert (if the no-alert rule checks for it)
alert("This is an alert");

// Implied eval
const evaluate = "eval(\"console.log('Implied eval')\")";

// Unused variable
const unusedVariable = "I am not used";

// Async function without await
async function fetchData() {
  // Some asynchronous code without await
}

// This code snippet contains various anti-patterns based on the rules you've mentioned.
