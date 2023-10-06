function getListStudentIds(studentList) {
    if (!Array.isArray(studentList)) {
      return [];
    }
  
    const studentIds = studentList.map((student) => {
      return student.id;
    });
  
    return studentIds;
  }
  
  export default getListStudentIds;
  