let el = document.querySelector('#red_header');
el.addEventListener('click', function() {
  let header = document.querySelector('header');
  header.classList.add('red');
});
