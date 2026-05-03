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

document.addEventListener('DOMContentLoaded', () => {
  const VISIBLE = 3;
  document.querySelectorAll('.content ul').forEach(ul => {
    const items = ul.querySelectorAll('li');
    if (items.length <= VISIBLE) return;

    items.forEach((li, i) => { if (i >= VISIBLE) li.hidden = true; });

    const toggle = document.createElement('a');
    toggle.href = '#';
    toggle.className = 'link timeline-toggle';
    toggle.textContent = 'See more…';
    ul.after(toggle);

    toggle.addEventListener('click', e => {
      e.preventDefault();
      const expanded = toggle.textContent === 'See less';
      items.forEach((li, i) => { if (i >= VISIBLE) li.hidden = expanded; });
      toggle.textContent = expanded ? 'See more…' : 'See less';
    });
  });
});

document.addEventListener('DOMContentLoaded', () => {
  const revealEls = document.querySelectorAll(
    '.about-wrapper, .achievement, .skills-group, .personal-block, .percurso, .project-card, .contact-wrapper, .centerTitles'
  );

  revealEls.forEach(el => el.classList.add('reveal'));

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        setTimeout(() => entry.target.classList.add('visible'), i * 80);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });

  revealEls.forEach(el => observer.observe(el));
});

document.addEventListener('DOMContentLoaded', () => {
    const button = document.getElementById('toggleProjects');

    button.addEventListener('click', () => {
      const hidden = document.querySelectorAll('.project-card--hidden');
      const isShowingMore = button.textContent.includes('More');

      hidden.forEach(card => {
        card.style.display = isShowingMore ? 'flex' : 'none';
      });

      button.textContent = isShowingMore ? 'Show Less Projects ↑' : 'Show More Projects ↓';
    });
});
