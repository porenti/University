// Функция нажатия на кнопку "поиск"
async function b_search() {
  let _insert = document.getElementById('here-searched'),
  _modal = new bootstrap.Modal(document.getElementById('modal-search')),
  _inp = document.getElementById('input-search').value;
  _insert.innerHTML = '';
  if (_inp.length != 0) {
    fetch(`/getall/${_inp}`, {
      method: 'GET',
      redirect: 'follow'
    })
      .then(response => response.json())
      .then(result => {
        if (result.length == 0)
          _insert.innerHTML = `
            <a class="list-group-item list-group-item-action" style="cursor: pointer;">
              <span>Поиск не дал результата...</span>
            </a>
          `;
        else
          for (let _item of result)
            _insert.innerHTML += `
              <a class="list-group-item list-group-item-action" style="cursor: pointer;" href="/quest/play?id=${_item.pk}">
                <span>${_item['Название']}</span>
              </a>
            `;
      });
  } else
    _insert.innerHTML = `
      <a class="list-group-item list-group-item-action" style="cursor: pointer;">
        <span>Поиск не дал результата...</span>
      </a>
    `;
  _modal.toggle();
}