// Коннектим переменные с DOM-объектами (строка поиска и кнопка "искать")
let inputSearch = document.getElementById('input-search'),
    buttonSearch = document.getElementById('button-search');

// Функция нажатия на кнопку "поиск"
async function buttonSearch.onclick = () => {
    fetch(`/getall/${inputSearch}`, {
        method: 'GET',
        redirect: 'follow'
    })
        .then(response => response.text())
        .then(result => console.log(result))
        .then(error => console.log('error', error));
}