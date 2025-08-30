function list() {
      let taskInput = document.getElementById("task-input");
      let taskValue = taskInput.value.trim();

      if (taskValue !== "") {
        let L=document.getElementById("task-list")
        L.innerHTML=L.innerHTML+"<li>"+taskValue+"</li>"
        taskInput.value = ""; // clear input after adding
      }
}