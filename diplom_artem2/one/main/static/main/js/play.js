// Функция поиска GET-параметров
function findGetParameter(parameterName) {
  let result = null,
    tmp = [];
  location.search
    .substr(1)
    .split("&")
    .forEach(function (item) {
      tmp = item.split("=");
      if (tmp[0] === parameterName) result = decodeURIComponent(tmp[1]);
    });
  return result;
}

if (findGetParameter('id') !== null) {
  document.getElementById('cont-play').style.display = 'none';
  fetch(`/getpk/${findGetParameter('id')}`, {
    method: 'GET',
    redirect: 'follow'
  })
    .then(response => response.json())
    .then(result => {
      console.log(result);
      document.getElementById('header-name').innerHTML = result['Название'];
    })
} else
  location.href = '/';