# NodeJS Basics

## Description
This project covers the basics of NodeJS, including how to run JavaScript using Node, how to use Node modules, file reading, process access, creating HTTP servers with Node and Express, and more.

## Resources
Read or watch:
- Node JS getting started
- Process API doc
- Child process
- Express getting started
- Mocha documentation
- Nodemon documentation

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
- run javascript using NodeJS
- use NodeJS modules
- use specific Node JS module to read files
- use process to access command line arguments and the environment
- create a small HTTP server using Node JS
- create a small HTTP server using Express JS
- create advanced routes with Express JS
- use ES6 with Node JS with Babel-node
- use Nodemon to develop faster

## Requirements
- Allowed editors: vi, vim, emacs, Visual Studio Code
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using node (version 20.x.x)
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the js extension
- Your code will be tested using Jest and the command npm run test
- Your code will be verified against lint using ESLint
- Your code needs to pass all the tests and lint. You can verify the entire project running npm run full-test
- All of your functions/classes must be exported by using this format: module.exports = myFunction;

## Tasks

### 0. Executing basic javascript with Node JS
Create a function named `displayMessage` that prints in STDOUT the string argument.

### 1. Using Process stdin
Create a program named `1-stdin.js` that will be executed through command line with interactive input.

### 2. Reading a file synchronously with Node JS
Create a function `countStudents` in the file `2-read_file.js` that reads a CSV database file synchronously.

### 3. Reading a file asynchronously with Node JS
Create a function `countStudents` in the file `3-read_file_async.js` that reads a CSV database file asynchronously.

### 4. Create a small HTTP server using Node's HTTP module
Create a small HTTP server using the http module in the file `4-http.js`.

### 5. Create a more complex HTTP server using Node's HTTP module
Create a more complex HTTP server in the file `5-http.js` with multiple routes.

### 6. Create a small HTTP server using Express
Create a small HTTP server using Express module in the file `6-http_express.js`.

### 7. Create a more complex HTTP server using Express
Create a more complex HTTP server using Express in the file `7-http_express.js`.

### 8. Organize a complex HTTP server using Express
Create a full server with proper organization in a directory named `full_server`.
