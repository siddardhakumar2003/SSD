import React, { useState, useEffect, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { setTodos, addTodo, removeTodo } from "../redux/todoSlice";
import axios from "axios";
import "./style.css";

export default function TaskApp() {
  const [taskText, setTaskText] = useState("");
  const tasks = useSelector((state) => state.todos.todos);
  const dispatch = useDispatch();
  const draggedItem = useRef(null);
  const [localTasks, setLocalTasks] = useState([]);

  // Load todos sorted by 'order'
  useEffect(() => {
    const fetchTodos = async () => {
      try {
        const res = await axios.get("http://localhost:5001/todos", { withCredentials: true });
        const sortedTodos = res.data.sort((a, b) => a.order - b.order);
        dispatch(setTodos(sortedTodos));
        setLocalTasks(sortedTodos);
      } catch (err) {
        console.error("Failed to fetch todos:", err);
      }
    };

    fetchTodos();
  }, [dispatch]);

  // Add todo
  const handleAddTask = async (e) => {
    e.preventDefault();
    const text = taskText.trim();
    if (!text) return;

    try {
      const res = await axios.post(
        "http://localhost:5001/todos",
        { title: text },
        { withCredentials: true }
      );
      dispatch(addTodo(res.data));
      setLocalTasks([...localTasks, res.data]);
      setTaskText("");
    } catch (err) {
      console.error("Failed to add todo:", err);
    }
  };

  // Remove todo
  const handleRemoveTask = async (id) => {
    try {
      await axios.delete(`http://localhost:5001/todos/${id}`, { withCredentials: true });
      dispatch(removeTodo(id));
      setLocalTasks(localTasks.filter((t) => t.id !== id));
    } catch (err) {
      console.error("Failed to delete todo:", err);
    }
  };

  // Drag start
  const handleDragStart = (index) => {
    draggedItem.current = index;
  };

  // Drag over
  const handleDragOver = (e, index) => {
    e.preventDefault();
    const items = [...localTasks];
    const draggedItemContent = items[draggedItem.current];

    items.splice(draggedItem.current, 1);
    items.splice(index, 0, draggedItemContent);

    draggedItem.current = index;
    setLocalTasks(items);
  };

  // Drag end: update DB
  const handleDragEnd = async () => {
    const updatedTasks = localTasks.map((task, index) => ({ ...task, order: index }));
    dispatch(setTodos(updatedTasks));

    try {
      // Update each task individually
      for (const task of updatedTasks) {
        await axios.put(
          `http://localhost:5001/todos/${task.id}`,
          { title: task.title, content: task.content || "", order: task.order },
          { withCredentials: true }
        );
      }
    } catch (err) {
      console.error("Failed to update order in DB:", err);
    }
  };

  return (
    <div className="container">
      <h1>My Todo List</h1>

      <form onSubmit={handleAddTask}>
        <input
          type="text"
          placeholder="Enter a new task"
          required
          value={taskText}
          onChange={(e) => setTaskText(e.target.value)}
        />
        <button type="submit">Add Todo</button>
      </form>

      <ul>
        {localTasks.map((task, index) => (
          <li
            key={task.id}
            draggable
            onDragStart={() => handleDragStart(index)}
            onDragOver={(e) => handleDragOver(e, index)}
            onDragEnd={handleDragEnd}
          >
            <span>{task.title}</span>
            <button onClick={() => handleRemoveTask(task.id)}>Remove</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
