import React, { useState } from 'react';

function TodoList() {
  const [tasks, setTasks] = useState([]);
  const [inputValue, setInputValue] = useState('');

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    if (inputValue.trim()) {
      setTasks([...tasks, { id: Date.now(), text: inputValue }]);
      setInputValue('');
    }
  };

  const handleDelete = (taskId) => {
    const updatedTasks = tasks.filter((task) => task.id !== taskId);
    setTasks(updatedTasks);
  };

  const handleEdit = (taskId, newText) => {
    const updatedTasks = tasks.map((task) =>
      task.id === taskId ? { ...task, text: newText } : task
    );
    setTasks(updatedTasks);
  };

  return (
    <div>
      <h1>To-do List</h1>
      <form onSubmit={handleSubmit}>
        <input type="text" value={inputValue} onChange={handleInputChange} />
        &nbsp;&nbsp;
        <button type="submit">Add Task</button>
      </form>
      <center>
      <ul>
        {tasks.map((task) => (
          <li key={task.id}>
            <span>{task.text}</span>&nbsp;&nbsp;
            <button onClick={() => handleDelete(task.id)}>Delete</button>&nbsp;&nbsp;
            <button onClick={() => handleEdit(task.id, prompt('Edit Task', task.text))}>Edit</button>
          </li>
        ))}
      </ul>
      </center>
    </div>
  );
}

export default TodoList;
