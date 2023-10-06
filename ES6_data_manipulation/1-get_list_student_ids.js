function getListStudentIds(studentList) {
    // Check if the input is an array
    if (!Array.isArray(studentList)) {
      return [];
    }
  
    // Use the map function to extract the IDs
    const studentIds = studentList.map((student) => {
      return student.id;
    });
  
    return studentIds;
  }
