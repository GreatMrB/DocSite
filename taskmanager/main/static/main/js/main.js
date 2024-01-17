function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
  }
  
  function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
  }
  
  const btn = document.querySelector(".btn-toggle");

btn.addEventListener("click", function () {
  document.body.classList.toggle("dark-theme");
});

feather.replace();


function myFunction() {
  document.getElementById("myDropdown2").classList.toggle("show");
}
window.onclick = function(event) {
  if (!event.target.matches('.dropbt')) {
    let dropdowns = document.getElementsByClassName("dropdown2-content");
    let i;
    for (i = 0; i < dropdowns.length; i++) {
      let openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}

function myFunction() {
  document.getElementById("myDropdowni").classList.toggle("show");
}
window.onclick = function(event) {
  if (!event.target.matches('.dropbtndoc')) {
    var dropdowns = document.getElementsByClassName("dropdown-contents");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}
















 
  