function darkMode() {
    var element = document.body;
    element.classList.toggle("darkMode");
      
}
  
document.getElementById('dark').addEventListener("click",darkMode);