const fs = require('fs');
const path = require('path');

function countStudents(filePath) {
  try {
    // Ensure we're using the correct path, resolving relative paths if needed
    const absolutePath = path.resolve(filePath);
    
    // Check if file exists before attempting to read
    if (!fs.existsSync(absolutePath)) {
      throw new Error('Cannot load the database');
    }
    
    // Read file synchronously
    const data = fs.readFileSync(absolutePath, 'utf8');
    const lines = data.trim().split('\n');
    
    // Skip header line and empty lines
    const students = lines.slice(1).filter((line) => line.trim().length > 0);
    
    console.log(`Number of students: ${students.length}`);
    
    // Group students by field
    const fields = {};
    students.forEach((student) => {
      const [firstName, lastName, age, field] = student.split(',');
      if (!fields[field]) {
        fields[field] = { count: 0, names: [] };
      }
      fields[field].count += 1;
      fields[field].names.push(firstName);
    });
    
    // Display students by field
    Object.keys(fields).forEach((field) => {
      console.log(`Number of students in ${field}: ${fields[field].count}. List: ${fields[field].names.join(', ')}`);
    });
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
