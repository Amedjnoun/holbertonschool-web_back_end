# ES6 Classes

## Description
This project focuses on understanding and implementing ES6 classes in JavaScript. You will learn how to define classes, add methods, use static methods, extend classes, and explore advanced concepts like metaprogramming and symbols.

---

## Resources
- [Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
- [Metaprogramming](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Meta_programming)

---

## Learning Objectives
By the end of this project, you should be able to:
- Define a class in JavaScript.
- Add methods to a class.
- Use static methods in a class.
- Extend a class from another class.
- Understand metaprogramming and symbols.

---

## Requirements
- **Environment**: Ubuntu 20.04 LTS, Node.js 20.x.x, npm 9.x.x.
- **Editors**: vi, vim, emacs, Visual Studio Code.
- **Code Style**: ESLint.
- **Testing**: Jest.
- **File Extensions**: `.js`.
- **Mandatory Files**: `README.md` at the root of the project.

---

## Setup Instructions

### Install Node.js
```bash
curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
```

### Verify Installation
```bash
nodejs -v
npm -v
```

### Install Dependencies
```bash
npm install --save-dev jest babel-jest @babel/core @babel/preset-env eslint
```

---

## Configuration Files
- **`package.json`**: Contains project metadata and dependencies.
- **`babel.config.js`**: Configures Babel for transpiling ES6+ code.
- **`.eslintrc.js`**: Configures ESLint for code linting.

---

## Tasks

### 0. ClassRoom
Define a `ClassRoom` class with a `maxStudentsSize` attribute.

### 1. Initialize Rooms
Create a function `initializeRooms` that returns an array of `ClassRoom` objects.

### 2. HolbertonCourse
Define a `HolbertonCourse` class with attributes `name`, `length`, and `students`. Add getters and setters for each attribute.

### 3. Currency
Define a `Currency` class with attributes `code` and `name`. Add a method `displayFullCurrency` to format the output.

### 4. Pricing
Define a `Pricing` class with attributes `amount` and `currency`. Add a method `displayFullPrice` and a static method `convertPrice`.

### 5. Building
Define an abstract `Building` class with a `sqft` attribute. Ensure subclasses implement `evacuationWarningMessage`.

### 6. SkyHighBuilding
Extend `Building` to create `SkyHighBuilding` with an additional `floors` attribute. Override `evacuationWarningMessage`.

### 7. Airport
Define an `Airport` class with attributes `name` and `code`. Override the default string description to return the airport code.

### 8. HolbertonClass
Define a `HolbertonClass` with attributes `size` and `location`. Cast the class to a `Number` or `String`.

### 9. Hoisting
Fix the provided code to ensure proper class hoisting and functionality.

### 10. Car
Define a `Car` class with attributes `brand`, `motor`, and `color`. Add a `cloneCar` method using ES6 symbols.

---

## Testing
Run the following command to test your code:
```bash
npm run test
```

To verify linting and tests:
```bash
npm run full-test
```

---

## Repository
- **GitHub Repository**: `holbertonschool-web_back_end`
- **Directory**: `ES6_classes`

---  