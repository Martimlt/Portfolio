document.addEventListener('DOMContentLoaded', function () {
  function toggleMenu() {
      var x = document.getElementById("myTopnav");
      if (x.className === "topnav") {
          x.className += " responsive";
      } else {
          x.className = "topnav";
      }
  }

  document.querySelector('.topnav .icon').addEventListener('click', toggleMenu);

  function closeMenu() {
      var x = document.getElementById("myTopnav");
      if (x.className.includes("responsive")) {
          x.className = "topnav";
      }
  }

  document.querySelectorAll('.topnav a:not(.icon)').forEach(item => {
      item.addEventListener('click', closeMenu);
  });
});
