const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer(async (req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  
  const { url } = req;
  
  if (url === '/') {
    res.end('Hello Holberton School!');
  } else if (url === '/students') {
    res.write('This is the list of our students\n');
    
    try {
      const databaseFile = process.argv[2];
      const { students, fields } = await countStudents(databaseFile);
      
      res.write(`Number of students: ${students.length}\n`);
      
      Object.keys(fields).forEach((field) => {
        res.write(`Number of students in ${field}: ${fields[field].count}. List: ${fields[field].names.join(', ')}\n`);
      });
      
      res.end();
    } catch (error) {
      res.end(error.message);
    }
  } else {
    res.statusCode = 404;
    res.end('Not found');
  }
});

app.listen(1245);

module.exports = app;
