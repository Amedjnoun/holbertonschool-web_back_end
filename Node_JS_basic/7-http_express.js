const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  let response = 'This is the list of our students\n';
  
  try {
    const databaseFile = process.argv[2];
    const { students, fields } = await countStudents(databaseFile);
    
    response += `Number of students: ${students.length}\n`;
    
    Object.keys(fields).forEach((field) => {
      response += `Number of students in ${field}: ${fields[field].count}. List: ${fields[field].names.join(', ')}\n`;
    });
    
    res.send(response);
  } catch (error) {
    response += error.message;
    res.send(response);
  }
});

app.listen(port);

module.exports = app;
