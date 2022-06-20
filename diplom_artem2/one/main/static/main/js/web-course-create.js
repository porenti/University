// Объявляем переменные roles pools и questions для сохранения туда данных о ролях, пулах и вопросах.
// Объявляем объект-ссылку на DOM-объекты (Document Object Model (Объектаная модель документа)) link_add_roles, link_add_pool, link_add_question.

let roles = {},
    pools = [],
    questions = [],
    link_add_roles = document.getElementById('link-add-roles'),
    link_add_pool = document.getElementById('link-add-pool'),
    link_add_question = document.getElementById('link-create-question');

// Функции работы с группами

// Функция, привязанная (забиндена) на нажатие по кнопке "Добавить роль". Собственно, добавляет новую роль.
link_add_roles.onclick = () => {
    let _id = `${+ new Date()}-roles`;
    roles[_id] = {
        name: null
    };
    let li = document.createElement('li');
    li.classList.add('list-group-item');
    li.id = `block-for-roles-${_id}`;
    li.innerHTML = `
        <div class="row">
            <div class="col-11">
                <input class="form-control" type="text" placeholder="Введите наименование роли..." id="role-input-${_id}" oninput="editNameOfRole('${_id}');" />
            </div>
            <div class="col-1 d-flex justify-content-center align-items-center" style="cursor: pointer;" onclick="deleteFromGroup('${_id}');">
                <i class="icon-close"></i>
            </div>
        </div>
    `;
    document.getElementById('group-of-roles').appendChild(li);
    editListInPools();
}

// Функция, отвечающая за удаление группы из списка
function deleteFromGroup(_id) {
    document.getElementById(`block-for-roles-${_id}`).remove();
    roles[_id] = undefined;
    editListInPools();
}

// Функция, отвечающая за обновление списка пулов во всех селектах
function editListInPools() {
    let lists = document.getElementsByClassName('list-of-roles');
    if (lists.length != 0) {
        for (let item of lists) {
            let htmlRoles = '<option value="thumb">Выберите значение</option>';
            for (let role in roles)
                if (roles[role] !== undefined) {
                   htmlRoles += `
                        <option ${role == item.value ? 'selected' : ''} value="${role}">${roles[role].name === null ? 'Не задано имя!' : roles[role].name}</option>
                    `;
                    if (role == item.value)
                        pools[item.getAttribute('data-id')].forWhom = role;
                }
            item.innerHTML = htmlRoles;
        }
    }
}

// Функция, отвечающая за обновление имени пула.
function editNameOfRole(_id) {
    let settedName = document.getElementById(`role-input-${_id}`).value;
    roles[_id].name = settedName;
    editListInPools();
}

// Функции работы с пулами

link_add_pool.onclick = () => {
    let _id = `${+ new Date()}-pools`;
    pools[_id] = {
        name: null,
        forWhom: null,
    };
    let div = document.createElement('div');
    div.classList.add('col-6');
    div.id = `block-for-pools-${_id}`;
    div.innerHTML = `
        <div style="padding: 15px;margin: 15px;background: var(--bs-light); border-radius: 15px;">
            <div class="row">
                <div class="col-11" style="margin: 15px 0;">
                    <label class="form-label">Наименование пула</label>
                    <input class="form-control" type="text" placeholder="Имя пула" data-id="${_id}" oninput="editPool(this, '${_id}', 'name');" />
                </div>
                <div class="col-1" style="margin: 15px 0;">
                    <i class="text-secondary icon-close" style="cursor: pointer;" onclick="erasePool('${_id}');"></i>
                </div>
            </div>
            <div class="row">
                <div class="col" style="margin: 15px 0;">
                    <label class="form-label">Для какой роли</label>
                    <select class="form-select list-of-roles" data-id="${_id}" oninput="editPool(this, '${_id}', 'forWhom');"></select>
                </div>
            </div>
        </div>
    `;
    document.getElementById('block-of-pools').appendChild(div);
    editListInPools();
    updateListOfPullsInQuestions();
}

function erasePool(_id) {
    document.getElementById(`block-for-pools-${_id}`).remove();
    pools[_id] = undefined;
    updateListOfPullsInQuestions();
}

function editPool(_t, _id, _type) {
    pools[_id][_type] = _t.value;
    updateListOfPullsInQuestions();
}

// Функции работы с вопросами

link_add_question.onclick = () => {
    let _id = `${+ new Date()}-questions`;
    questions[_id] = {
        name: null,
        pool_id: null,
        type: 'text',
        question: null,
        answer: null
    };
    let div = document.createElement('div');
    div.classList.add('row');
    div.id = `block-for-questions-${_id}`;
    div.style.marginBottom = '15px';
    div.innerHTML = `
        <div class="col">
            <h5 style="font-family: 'Montserrat Alternates', sans-serif;">Вопрос</h5>
            <input class="form-control" type="text" oninput="editQuestion(this, '${_id}', 'name');" placeholder="Введите имя вопроса">
        </div>
        <div class="col">
            <div class="row" style="margin-bottom: 15px;">
                <div class="col">
                    <label class="form-label">Тип вопроса:</label>
                    <select class="form-select" oninput="editQuestion(this, '${_id}', 'type');">
                        <option value="text" selected>Текстовый</option>
                        <option value="truefalse">Верно/неверно</option>
                    </select>
                </div>
            </div>
            <div class="row" style="margin-bottom: 15px;">
                <div class="col">
                    <label class="form-label">Для какого пула:</label>
                    <select class="form-select list-of-pools" oninput="editQuestion(this, '${_id}', 'pool_id');"></select>
                </div>
            </div>
            <div class="row" style="margin-bottom: 15px;">
                <div class="col">
                    <label class="form-label">Введите текст вопроса:</label>
                    <textarea class="form-control" oninput="editQuestion(this, '${_id}', 'question');"></textarea>
                </div>
            </div>
            <div class="row" style="margin-bottom: 15px;" id="chooser-of-answer-${_id}">
                <div class="col">
                    <label class="form-label">Введите правильный ответ:</label>
                    <textarea class="form-control" oninput="editQuestion(this, '${_id}', 'answer');"></textarea>
                </div>
            </div>
        </div>
    `;
    document.getElementById('block-of-questions').appendChild(div);
    updateListOfPullsInQuestions();
}

function updateListOfPullsInQuestions() {
    let lists = document.getElementsByClassName('list-of-pools');
    if (lists.length != 0) {
        for (let item of lists) {
            let htmlRoles = '<option value="thumb">Выберите значение</option>';
            for (let pool in pools)
                if (pools[pool] !== undefined) {
                   htmlRoles += `
                        <option ${pool == item.value ? 'selected' : ''} value="${pool}">${pools[pool].name === null ? 'Не задано у пула!' : pools[pool].name}</option>
                    `;
                }
            item.innerHTML = htmlRoles;
        }
    }
}

function editQuestion(_t, _id, _type) {
    if (_type == 'type') {
        let _insertHTML;
        switch (_t.value) {
            case 'text':
                _insertHTML = `
                    <div class="col">
                        <label class="form-label">Введите правильный ответ:</label>
                        <textarea class="form-control" oninput="editQuestion(this, '${_id}', 'answer');"></textarea>
                    </div>
                `;
            break;
            case 'truefalse':
                let _cId = + new Date();
                _insertHTML = `
                    <div ckass="col">
                        <div class="form-check">
                            <input id="answer-checkbox-${_cId}" class="form-check-input" type="checkbox" oninput="editQuestion(this, '${_id}', 'answer');">
                            <label class="form-check-label" for="answer-checkbox-${_cId}">Если правильный ответ "истина", то отметьте</label>
                        </div>
                    </div>
                `;
            break;
        }
        document.getElementById(`chooser-of-answer-${_id}`).innerHTML = _insertHTML;
    }
    questions[_id][_type] = _t.value;
}

// Функция отправки на сервер
async function sendToServer() {
    let _headers = new Headers(),
        _raw = JSON.stringify({

        })
    _headers.append('Content-Type', 'application/json');
    let _reqOptions = {
        method: 'POST',
        headers: _headers,
        body: _raw,
        redirect: 'follow'
    };

    fetch('http/127.0.0.1:8000/quest/', _reqOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .then(error => console.log('error', error));
}