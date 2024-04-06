
// Faculty Evaluation Average Ratings
const valueToSet = json_data.overall_avg_first;
const valueToSetTwo = json_data.overall_avg_second;

// Present Faculty Rating: First Semester
const frfs = document.getElementById('frfs');
frfs.textContent = valueToSet;

// Present Faculty Rating: Second Semester
const frss = document.getElementById('frss');
frss.textContent = valueToSetTwo;
