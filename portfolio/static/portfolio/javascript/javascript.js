document.getElementById('hamburger').addEventListener('click', function() {
    var navLinks = document.getElementById('navLinks');
    navLinks.classList.toggle('show');
});

function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
      x.className += " responsive";
    } else {
      x.className = "topnav";
    }
}

document.addEventListener('DOMContentLoaded', function() {
  fetch('https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json')// envia GET request ao URL
  .then(response => response.json()) // põe os dados na consola
  .then(data => {
      const tempMax = data.data[0].tMax;
      const tempMin = data.data[0].tMin
      document.getElementById('tempMax').innerHTML = tempMax
      document.getElementById('tempMin').innerHTML = tempMin
  });
  return false;
});