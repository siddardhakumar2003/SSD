const form = document.getElementById('task-form');
const input = document.getElementById('task-input');
const taskList = document.getElementById('task-list');

let draggedItem = null;

// Part 1
form.addEventListener('submit', (e) => {
  e.preventDefault(); 
  const taskText = input.value.trim();
  if (taskText === '') return;

  const li = document.createElement('li');
  li.textContent = taskText;
  li.draggable = true;

  // Create Remove button
  const removeBtn = document.createElement('button');
  removeBtn.textContent = 'Remove';
  li.appendChild(removeBtn);

  taskList.appendChild(li);
  input.value = ''; 
});

// Part 2
taskList.addEventListener('click', (e) => {
  if (e.target.tagName === 'BUTTON') {
    const li = e.target.parentElement;
    li.remove();
  }
});

// Part 3
taskList.addEventListener('dragstart', (e) => {
  draggedItem = e.target;
  e.target.classList.add('dragging');
});

taskList.addEventListener('dragend', (e) => {
  e.target.classList.remove('dragging');
  draggedItem = null;
});

taskList.addEventListener('dragover', (e) => {
  e.preventDefault(); 
  const afterElement = getDragAfterElement(taskList, e.clientY);
  if (afterElement == null) {
    taskList.appendChild(draggedItem);
  } else {
    taskList.insertBefore(draggedItem, afterElement);
  }
});

function getDragAfterElement(container, y) {
  const draggableElements = [...container.querySelectorAll('li:not(.dragging)')];

  return draggableElements.reduce((closest, child) => {
    const box = child.getBoundingClientRect();
    const offset = y - box.top - box.height / 2;
    if (offset < 0 && offset > closest.offset) {
      return { offset: offset, element: child };
    } else {
      return closest;
    }
  }, { offset: Number.NEGATIVE_INFINITY }).element;
}
