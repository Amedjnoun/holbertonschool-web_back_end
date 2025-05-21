const fs = require('fs').promises;

async function countStudents(path) {
  try {
    // Read file asynchronously
    const data = await fs.readFile(path, 'utf8');
    const lines = data.trim().split('\n');
    
    // Skip header line and empty lines
    const students = lines.slice(1).filter((line) => line.trim().length > 0);
    
    console.log(`Number of students: ${students.length}`);
    
    // Group students by field
    const fieldGroups = {};
    
    for (const student of students) {
      const studentData = student.split(',');
      const firstName = studentData[0];
      const field = studentData[3];
      
      if (!fieldGroups[field]) {
        fieldGroups[field] = [];
      }
      
      fieldGroups[field].push(firstName);
    }
    
    // Display students by field
    for (const [field, names] of Object.entries(fieldGroups)) {
      console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
    }
    
    return { students, fieldGroups };
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
