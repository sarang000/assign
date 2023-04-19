import React, { useState } from "react";
import "./App.css";

const courseData = [
  {
    id: 1,
    name: "Introduction to ReactJS",
    instructor: "Pavan",
    duration: "4 weeks",
    description:
      "Basics of reatJS.",
  },
  {
    id: 2,
    name: "C++ for Beginners",
    instructor: "Somu",
    duration: "6 weeks",
    description:
      "Basics of C++.",
  },
  {
    id: 3,
    name: "Python",
    instructor: "Aditya",
    duration: "8 weeks",
    description:
      "Basics of python.",
  },
];

function Login({ onLogin }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  

  const handleSubmit = (e) => {
    e.preventDefault();
    // Check username and password
    if (username === "user" && password === "password") {
      onLogin();
    } else {
      alert("Incorrect username or password. Please try again.");
    }
  };

  return (
    <form claas="a"onSubmit={handleSubmit}>
      <img src={require("./1.gif")}/>
      <h1>Login</h1>
      <div>
        <label htmlFor="username">Username:</label>
        <input type="text" id="username" value={username} onChange={(e) => setUsername(e.target.value)} />
      </div>
      <div>
        <label htmlFor="password">Password:</label>
        <input type="password" id="password" value={password} onChange={(e) => setPassword(e.target.value)} />
      </div>
      <button type="submit">Login</button>
    </form>
  );
}

function CourseList({ courses, onCourseSelect }) {
  return (
    <div>
      {courses.map((course) => (
        <div key={course.id} className="course" onClick={() => onCourseSelect(course)}>
          <h2>{course.name}</h2>
          <p>Instructor: {course.instructor}</p>
        </div>
      ))}
    </div>
  );
}

function CourseDetails({ course }) {
  return (
    <div>
      <h1>{course.name}</h1>
      <p>Instructor: {course.instructor}</p>
      <p>Duration: {course.duration}</p>
      <p>Description: {course.description}</p>
    </div>
  );
}

function App() {
  const [loggedIn, setLoggedIn] = useState(false);
  const [selectedCourse, setSelectedCourse] = useState(null);
  const [searchTerm, setSearchTerm] = useState("");

  const handleLogin = () => {
    setLoggedIn(true);
  };

  const handleLogout = () => {
    setLoggedIn(false);
    setSelectedCourse(null);
    setSearchTerm("");
  };

  const handleCourseSelect = (course) => {
    setSelectedCourse(course);
  };

  const handleCourseDeselect = () => {
    setSelectedCourse(null);
  };

  const handleSearch = (e) => {
    setSearchTerm(e.target.value);
  };

  const filteredCourses = courseData.filter((course) => course.name.toLowerCase().includes(searchTerm.toLowerCase()));

  return (
    <div className="App">
      {loggedIn ? (
        <>
          {!selectedCourse ? (
            <>
              <h1>Course Catalog</h1>
              <div>
                <label htmlFor="search">Search:</label>
                <input type="text" id="search" value={searchTerm} onChange={handleSearch} />
              </div>
              <CourseList courses={filteredCourses} onCourseSelect={handleCourseSelect} />
            </>
          ) : (
            <>
              <button onClick={handleCourseDeselect}>Back to Course Catalog</button>
              <CourseDetails course={selectedCourse} />
            </>
          )}
          <button onClick={handleLogout}>Logout</button>
        </>
      ) : (
        <Login onLogin={handleLogin} />
      )}
    </div>
  );
}

export default App;

