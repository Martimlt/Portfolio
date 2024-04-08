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

document.addEventListener('DOMContentLoaded', (event) => {
    function toggleProjects() {
      const projectsContainer = document.getElementById('projectsContainer');
      const projects = projectsContainer.children;
      const button = document.getElementById('toggleProjects');
      
      let showMore = button.textContent.includes('More');
      for (let i = 5; i < projects.length; i++) {
        if (showMore) {
          projects[i].style.display = ''; // Reverts to CSS default instead of forcing 'block'
        } else {
          projects[i].style.display = 'none';
        }
      }
      
      button.textContent = showMore ? 'Show Less Projects ↑' : 'Show More Projects ↓';
    }

    // Initially hide projects beyond the first five
    const projectsContainer = document.getElementById('projectsContainer');
    const projects = projectsContainer.children;
    for (let i = 5; i < projects.length; i++) {
      projects[i].style.display = 'none';
    }

    // Attach the toggle function to the button without using inline JavaScript
    document.getElementById('toggleProjects').addEventListener('click', toggleProjects);
  });
