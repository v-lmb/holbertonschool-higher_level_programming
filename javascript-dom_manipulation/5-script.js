let el = document.querySelector('#update_header');

el.addEventListener('click', function() {
  let li = document.querySelector('header');
  li.textContent = 'New Header!!!';
});
