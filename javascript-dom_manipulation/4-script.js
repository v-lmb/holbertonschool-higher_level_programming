let el = document.querySelector('#add_item');
let ul = document.querySelector('.my_list');

el.addEventListener('click', function() {
  let li = document.createElement('li');
  li.textContent = 'Item';
  ul.appendChild(li);
});
