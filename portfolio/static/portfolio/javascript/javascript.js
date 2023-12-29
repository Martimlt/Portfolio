function myFunction() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}

// Function to close the dropdown menu
function closeMenu() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav responsive") {
    x.className = "topnav";
  }
}

// Add event listeners to each menu item
document.querySelectorAll('.topnav a').forEach(item => {
  item.addEventListener('click', closeMenu);
});
