// Prevent Bootstrap dialog from blocking focusin
document.addEventListener('focusin', (e) => {
    if (e.target.closest(".tox-tinymce, .tox-tinymce-aux, .moxman-window, .tam-assetmanager-root") !== null) {
      e.stopImmediatePropagation();
    }
  });

let _questionsCounter = 0;          // Счетчик количества созданных вопросов

// Функция, вызываемая по событию onclick на кнопку "Добавить вопрос"
document.getElementById('link-insert-question').onclick = () => {
    let _questions = document.getElementById('container-questions'),
    _question = document.createElement('li');

    _questionsCounter++;

    _question.classList.add('list-group-item');
    _question.setAttribute('data-counter', _questionsCounter);
    _question.id = `question-item-${_questionsCounter}`;
    _question.innerHTML = `
        <div class="row">
            <div class="col-3 col-sm-2 col-md-2 col-lg-1" style="margin-top: 15px;">
                <button class="btn btn-danger btn-sm" type="button" onclick="removeById('${_question.id}');">
                    <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16" class="bi bi-x-lg">
                        <path fill-rule="evenodd" d="M13.854 2.146a.5.5 0 0 1 0 .708l-11 11a.5.5 0 0 1-.708-.708l11-11a.5.5 0 0 1 .708 0Z"></path>
                        <path fill-rule="evenodd" d="M2.146 2.146a.5.5 0 0 0 0 .708l11 11a.5.5 0 0 0 .708-.708l-11-11a.5.5 0 0 0-.708 0Z"></path>
                    </svg>
                </button>
            </div>
            <div class="col-9 col-sm-10 col-md-10 col-lg-5" style="margin-top: 15px;">
                <div class="input-group">
                    <span class="input-group-text">Название вопроса:</span>
                    <input class="form-control" type="text" placeholder="Вот тут!" name="name-of-question" required="">
                </div>
            </div>
            <div class="col-12 col-sm-12 col-md-12 col-lg-6" style="margin-top: 15px;">
                <ul class="list-group sources-list" id="list-of-sources-${_questionsCounter}"></ul>
                <button class="btn btn-secondary btn-sm float-end" type="button" style="margin-top: 10px;" data-counter="0" onclick="addResourse(this, 'list-of-sources-${_questionsCounter}');">Добавить источник</button>
            </div>
            <div class="col-12" style="margin-top: 15px;">
                <h4>Текст вопроса</h4>
                <div class="wysiwyg" id="wysiwyg-${_questionsCounter}"></div>
            </div>
            <div class="col-12 col-sm-12 col-md-12 col-lg-6" style="margin-top: 15px;">
                <h4>Тип ответа</h4>
                <select class="form-select" name="type-of-question" oninput="selectOfType(this, ${_questionsCounter});">
                    <option value="text" selected="">Текстовый ответ</option>
                    <option value="truefalse">Верно/неверно</option>
                    <option value="choose">Один из нескольких</option>
                </select>
            </div>
            <div class="col-12 col-sm-12 col-md-12 col-lg-6" style="margin-top: 15px;">
                <h4>Правильный ответ</h4>
                <div id="select-right-answer-${_questionsCounter}">
                    <input class="form-control" name="right-answer" type="text" placeholder="Введите ответ" required="">
                </div>
            </div>
            <div class="col-12" style="margin-top: 15px;">
                <h4>Введите букву!</h4>
                <input class="form-control" type="text" name="char-of-question" placeholder="Вот тут введите вашу букву">
            </div>
        </div>
    `;

    _questions.appendChild(_question);
    tinymce.init({
        selector: `#wysiwyg-${_questionsCounter}`,
        placeholder: 'Начните описывать вопрос...',
        language: 'ru',
        toolbar: 'undo redo | blocks | bold italic backcolor | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | removeformat | help',
        plugins: [
            'advlist', 'autolink', 'lists', 'link', 'image', 'charmap', 'preview',
            'anchor', 'searchreplace', 'visualblocks', 'code', 'fullscreen',
            'insertdatetime', 'media', 'table', 'help', 'wordcount'
        ],
        height: 500,
        file_picker_callback: (callback, value, meta) => {
            if (meta.filetype == 'file')
                callback('mypage.html', { text: 'My text' });
            if (meta.filetype == 'image')
                callback('myimage.jpg', { alt: 'My alt text' });
            if (meta.filetype == 'media')
                callback('movie.mp4', { source2: 'alt.ogg', poster: 'image.jpg' });
        }
    });
}

// Функция, которая удаляет элемент из DOM по его id
function removeById(_id) {
    document.getElementById(_id).remove();
}

// Функция, которая добавляет новый источник в список источников вопроса
function addResourse(_t, _id) {
    let _counter = Number(_t.getAttribute('data-counter')) + 1,
        _list = document.getElementById(_id),
        _li = document.createElement('li');

    _t.setAttribute('data-counter', _counter);

    _li.classList.add('list-group-item');
    _li.id = `item-of-sources-${_counter}`;
    _li.innerHTML = `
        <div class="input-group">
            <input class="form-control" type="text" required="" name="sources-name" placeholder="Название источника" />
            <input class="form-control" type="text" required="" name="sources-link" placeholder="Ссылка на источник" />
            <button class="btn btn-danger" type="button" onclick="removeById('item-of-sources-${_counter}');">
                <svg class="bi bi-x-lg" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M13.854 2.146a.5.5 0 0 1 0 .708l-11 11a.5.5 0 0 1-.708-.708l11-11a.5.5 0 0 1 .708 0Z"></path>
                    <path fill-rule="evenodd" d="M2.146 2.146a.5.5 0 0 0 0 .708l11 11a.5.5 0 0 0 .708-.708l-11-11a.5.5 0 0 0-.708 0Z"></path>
                </svg>
            </button>
        </div>
    `;

    _list.appendChild(_li);
}

// Функция, которая изменет тип ответа
function selectOfType(_t, _cnt) {
    let _insertWhere = document.getElementById(`select-right-answer-${_cnt}`);
    switch (_t.value) {
        case 'text':
            _insertWhere.innerHTML = `<input class="form-control" name="right-answer" type="text" placeholder="Введите ответ" required="">`;
        break;
        case 'truefalse':
            _insertWhere.innerHTML = `
                <select class="form-select" name="right-answer" required="">
                    <option value="true" selected="">Верно</option>
                    <option value="false">Неверно</option>
                </select>
            `;
        break;
        case 'choose':
            let _timestamp = + new Date();
            _insertWhere.innerHTML = `
                <ul class="list-group chooser-options" id="choose-ul-${_timestamp}"></ul>
                <div class="list-group" style="margin-top: 10px;">
                    <a class="list-group-item list-group-item-action list-group-item-primary text-center" data-counter="0" onclick="addChoose(this, 'choose-ul-${_timestamp}');" style="cursor: pointer;">
                        <span>Добавить вариант ответа</span>
                    </a>
                </div>
            `;
        break;
    }
}

// Функция, которая добавляет вариант ответа в тип вопроса choose
function addChoose(_t, _id) {
    let _where = document.getElementById(_id),
        _li = document.createElement('li'),
        _counter = Number(_t.getAttribute('data-counter')) + 1;

    _t.setAttribute('data-counter', _counter);
    
    _li.classList.add('list-group-item');
    _li.id = `${_id}-item-${_counter}`;
    _li.innerHTML = `
        <div class="input-group">
            <input class="form-control" name="name-of-option" type="text" placeholder="Вариант...">
            <span class="input-group-text">
                <input type="radio" name="radio-of-option">
            </span>
            <button class="btn btn-danger" type="button" onclick="removeById('${_id}-item-${_counter}');">
                <svg class="bi bi-x-lg" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M13.854 2.146a.5.5 0 0 1 0 .708l-11 11a.5.5 0 0 1-.708-.708l11-11a.5.5 0 0 1 .708 0Z"></path>
                    <path fill-rule="evenodd" d="M2.146 2.146a.5.5 0 0 0 0 .708l11 11a.5.5 0 0 0 .708-.708l-11-11a.5.5 0 0 0-.708 0Z"></path>
                </svg>
            </button>
        </div>
    `;
    _where.appendChild(_li);
}

// Функция, которая вычленяет из формы JSON-объект и передает его на сервер
function saveQuest() {
    _builder = {
        name: document.getElementById('quest-heading').value,
        description: document.getElementById('quest-description').value,
        questions: (() => {
            _questionsBuilder = [];
            for (let _question of document.getElementById('container-questions').childNodes)
                _questionsBuilder.push({
                    name: document.querySelector(`#${_question.id} [name="name-of-question"]`).value,
                    sources: (() => {
                        let _ret = [];
                        for (let _source of document.querySelectorAll(`#${_question.id} .sources-list > li`))
                            _ret.push({
                                name: document.querySelector(`#${_source.id} [name="sources-name"]`).value,
                                url: document.querySelector(`#${_source.id} [name="sources-link"]`).value
                            });
                        return _ret;
                    })(),
                    type: document.querySelector(`#${_question.id} [name="type-of-question"]`).value,
                    mainText: tinymce.get(document.querySelector(`#${_question.id} .wysiwyg`).id).getContent(),
                    answer: (() => {
                        let _ret;
                        switch (document.querySelector(`#${_question.id} [name="type-of-question"]`).value) {
                            case 'text':
                            case 'truefalse':
                                _ret = document.querySelector(`#${_question.id} [name="right-answer"]`).value;
                            break;
                            case 'choose':
                                _ret = [];
                                for (_option of document.querySelectorAll(`#${_question.id} .chooser-options > li`))
                                    _ret.push({
                                        name: _option.querySelector('[name="name-of-option"]').value,
                                        isMe: _option.querySelector('[name="radio-of-option"]').checked
                                    });
                            break;
                        }
                        return _ret;
                    })(),
                    char: document.querySelector(`#${_question.id} [name="char-of-question"]`).value,
                });
            return _questionsBuilder;
        })()
    };
    // console.log(JSON.stringify(_builder));
    localStorage.setItem('json_quest', JSON.stringify(_builder));
}