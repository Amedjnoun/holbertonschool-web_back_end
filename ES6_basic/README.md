# ES6 Basics

## Description
This project introduces the fundamental concepts of ECMAScript 6 (ES6), a major update to JavaScript. It covers new features, syntax improvements, and best practices for writing modern JavaScript code. By the end of this project, you will be able to explain and apply ES6 concepts effectively.

## Learning Objectives
At the end of this project, you should be able to:
- Understand what ES6 is and its significance.
- Identify new features introduced in ES6.
- Differentiate between constants (`const`) and variables (`let`).
- Use block-scoped variables.
- Write arrow functions and use default parameters.
- Utilize rest and spread function parameters.
- Implement string templating in ES6.
- Create objects and define their properties in ES6.
- Work with iterators and `for-of` loops.

## Requirements
- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using **Node.js 20.x.x** and **npm 9.x.x**.
- Use allowed editors: `vi`, `vim`, `emacs`, `Visual Studio Code`.
- All files should end with a new line.
- A `README.md` file at the root of the project is mandatory.
- Use the `.js` file extension for all code files.
- Code will be tested using the **Jest Testing Framework**.
- Code will be analyzed using **ESLint** with specific rules provided.
- All functions must be exported.

## Setup Instructions
### Install Node.js 20.x.x
```bash
curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
nodejs -v
npm -v
```

### Install Jest, Babel, and ESLint
```bash
npm install --save-dev jest
npm install --save-dev babel-jest @babel/core @babel/preset-env
npm install --save-dev eslint
```

### Configuration Files
Create the following configuration files in your project directory:
1. `package.json`
2. `babel.config.js`
3. `.eslintrc.js`

Run `npm install` to install all necessary dependencies. **Do not push the `node_modules` folder to your repository.**

## Tasks Overview
### 0. Const or let?
Refactor functions to use `const` and `let` instead of `var`.

### 1. Block Scope
Modify variables to prevent overwriting inside conditional blocks.

### 2. Arrow Functions
Rewrite a function using ES6 arrow syntax.

### 3. Parameter Defaults
Condense a function using default parameter values.

### 4. Rest Parameter Syntax
Use the rest parameter syntax to count the number of arguments passed to a function.

### 5. Spread Syntax
Concatenate arrays and strings using the spread syntax.

### 6. Template Literals
Rewrite a return statement using template literals.

### 7. Object Property Shorthand
Simplify object creation using property value shorthand syntax.

### 8. Computed Property Names
Use computed property names to dynamically define object keys.

### 9. ES6 Method Properties
Refactor methods in an object to use ES6 method property syntax.

### 10. For...of Loops
Rewrite a function to use the `for...of` loop.

### 11. Iterator
Create a function that returns an object with a department name and its employees.

### 12. Report Object
Create a report object with a method to count the number of departments.

## Execution Examples
Each task includes example input and output to demonstrate expected behavior. Refer to the task descriptions for detailed instructions.

## Repository Structure
```
holbertonschool-web_back_end/
└── ES6_basic/
    ├── 0-constants.js
    ├── 1-block-scoped.js
    ├── 2-arrow.js
    ├── 3-default-parameter.js
    ├── 4-rest-parameter.js
    ├── 5-spread-operator.js
    ├── 6-string-interpolation.js
    ├── 7-getBudgetObject.js
    ├── 8-getBudgetCurrentYear.js
    ├── 9-getFullBudget.js
    ├── 10-loops.js
    ├── 11-createEmployeesObject.js
    ├── 12-createReportObject.js
    └── README.md
```

## Author
**Johann Kerbrat**  
Engineering Manager at Uber Works  

## License
This project is part of the Holberton School curriculum.  