function person(){
  let userName = prompt("Please enter your name:");
  
  if (userName !== null && userName.trim() !== "") {
    document.getElementById("greeting-text").textContent = "Hello, " + userName + "!";
    document.getElementById("card-message").textContent = "Wishing you a wonderful day filled with joy and positivity!";
    document.getElementById("card").style.backgroundColor = "#ffe0b2"; // light peach
    document.getElementById("greeting-text").style.color = "#d84315"; // deep orange
  } else {
    alert("Name cannot be empty. Please try again!");
  }
}