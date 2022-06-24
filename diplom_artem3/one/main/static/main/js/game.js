let _wordIsShow = false, // Глобальный триггер, который хранит в себе значение, показ ли блок со словом
  _quest = JSON.parse(localStorage.getItem('json_quest')), // Тут хранится сам квест. Пока с localStorage, как Сережа сделает сервер -- через сервер
  _currentQuestion = 1, // Счетчик current вопроса
  _countOfQuestions = _quest.questions.length, // Общее количество вопросов
  _word = []; // Храним слово отдельно

// Начало глобальной инициализации квеста
document.getElementById('quest-name-heading').innerHTML = _quest.name; // Задаем имя квеста
document.getElementById('quest-description').innerHTML = _quest.description.replace('\n', '<br>'); // Задаем описание квеста

let _questionsBlocks = '',
  _questionsNumbers = '',
  _questionsWord = '',
  _questCounter = 0;
for (let question of _quest.questions) {
  _questCounter++;
  _questionsBlocks += `
    <div class="question-card" id="question-card-${_questCounter}" style="${_questCounter === 1 ? 'display:block;' : 'display:none;'}">
      <h4>${question.name}</h4>
      <div>
        ${question.mainText}
      </div>
      <div class="row" style="margin-top: 10px;">
        <div class="col-12">
          <h4>Ответ</h4>
        </div>
        <div class="col-12">
          <form>
            ${(() => {
              switch (question.type) {
                case 'text':
                  return `<input class="form-control" type="text" name="text-answer" placeholder="Введите ваш ответ">`;
                break;
                case 'truefalse':
                  return `
                    <ul class="list-group">
                      <li class="list-group-item">
                        <div class="form-check">
                          <input class="form-check-input" name="truefalse" value="true" type="radio" id="checkbox-true-${_questCounter}">
                          <label class="form-check-label" for="checkbox-true-${_questCounter}">Верно</label>
                        </div>
                      </li>
                      <li class="list-group-item">
                        <div class="form-check">
                          <input class="form-check-input" name="truefalse" value="false" type="radio" id="checkbox-false-${_questCounter}">
                          <label class="form-check-label" for="checkbox-false-${_questCounter}">Не верно</label>
                        </div>
                      </li>
                    </ul>
                  `;
                break;
                case 'choose':
                  return `
                    <ul class="list-group">
                      ${(() => {
                        let _ret = '',
                          _counter = 0;
                        
                        for (let answer of question.answer) {
                          _ret += `
                            <li class="list-group-item">
                              <div class="form-check">
                                <input class="form-check-input" type="radio" name="choose" value="${_counter}" id="checkbox-choose-${_questCounter}-${_counter}">
                                <label class="form-check-label" for="checkbox-choose-${_questCounter}-${_counter}">${answer.name}</label>
                              </div>
                            </li>
                          `;
                          _counter++;
                        }
                        return _ret;
                      })()}
                    </ul>
                  `;
                break;
              }
            })()}
          </form>
        </div>
        <div class="col-12">
          ${(() => {
            let _ret = '';
            if (question.sources.length != 0) {
              _ret += '<h4 style="margin-top: 10px;">Источники, которыми рекомендуем пользоваться</h4><div class="list-group d-flex flex-wrap">';
              for (let source of question.sources)
                _ret += `
                  <a class="list-group-item list-group-item-action" href="${source.url}" target="_blank">
                    <span>${source.name}</span>
                  </a>
                `;
              _ret += '</div>';
            }
            return _ret;
          })()}
        </div>
        ${(() => {
          if (_questCounter === _countOfQuestions) {
            return `
              <div class="col-12" style="margin: 10px 0;">
                <button class="btn btn-primary btn-lg" onclick="checkAnswers();" type="button">Проверить 👩‍🔬!</button>
              </div>
            `;
          } else return '';
        })()}
      </div>
    </div>
  `;
  _questionsNumbers += `
    <li id="question-number-${_questCounter}" class="list-group-item question-number ${_questCounter === 1 ? 'active' : ''}">
      <span>${_questCounter}</span>
    </li>
  `;
  _questionsWord += question.char.length === 1 ? `
    <li class="list-group-item" id='quest-word-char-${_questCounter}'>
      <span>
          <strong>*</strong>
      </span>
    </li>
  ` : '';
  _word.push(question.char.toUpperCase());
}

document.getElementById('questions-block').innerHTML = _questionsBlocks;
document.getElementById('quest-numbers').innerHTML = _questionsNumbers;
if (_questionsWord.length !== 0)
  document.getElementById('quest-word').innerHTML = _questionsWord;
else {
  document.getElementById('quest-word').remove();
  document.getElementById('show-word-block').remove();
}

// Конец глобальной инициализации квеста

// Функция нажатия на кнопку "показать блок со словом"
if (_questionsWord.length !== 0)
  document.getElementById('show-word-block').onclick = () => {
    if (_wordIsShow) {
      _wordIsShow = !_wordIsShow;
      document.getElementById('word-block').style.transform = 'translateY(0)';
      document.getElementById('show-word-block-icon').style.transform = 'rotate(180deg)';
    } else {
      _wordIsShow = !_wordIsShow;
      document.getElementById('word-block').style.transform = 'translateY(-10rem)';
      document.getElementById('show-word-block-icon').style.transform = 'rotate(0deg)';
    }
  }

// Функция нажатия на кнопку "Начинаем!"
document.getElementById('start-quest-button').onclick = () => {
  document.getElementById('start-card').style.display = 'none';
  document.getElementById('quest-landing').style.display = 'block';
}

// Функция нажатия на кнопки "Вперед" и "Назад"
function moveQuestion(_where) {
  switch (_where) {
    case 'back':
      _currentQuestion++;
      if (_countOfQuestions < _currentQuestion)
        _currentQuestion = 1;
    break;
    case 'forward':
      _currentQuestion--;
      if (_currentQuestion === 0)
        _currentQuestion = _countOfQuestions;
    break;
  }
  for (let item of document.querySelectorAll('.question-card'))
    item.style.display = 'none';
  document.getElementById(`question-card-${_currentQuestion}`).style.display = 'block';
  for (let item of document.querySelectorAll('.question-number'))
    item.classList.remove('active');
  document.getElementById(`question-number-${_currentQuestion}`).classList.add('active');
}

// Функция проверки ответов
function checkAnswers() {
  let _position = 1,
    _answers = [];
  for (let item of _quest.questions) {
    let _answer = {
      name: item.name,
      correctAnswer: (() => {
        switch (item.type) {
          case 'text':
          case 'truefalse':
            return item.answer;
          case 'choose':
            let _r = '';
            for (let i of item.answer)
              if (i.isMe)
                _r = i.name
            return _r;
        }
      })()
    };
    switch (item.type) {
      case 'text':
        _answer.isCorrect = document.querySelector(`#question-card-${_position} [name="text-answer"]`)
          .value
          .toUpperCase() == item
          .answer
          .toUpperCase();
        _answer.char = _answer.isCorrect ? item.char.toUpperCase() : '';
      break;
      case 'truefalse':
        let _choosen1 = document.querySelector(`#checkbox-true-${_position}`).checked,
          _correct = item.answer == 'true';
        _answer.isCorrect = _choosen1 == _correct;
        _answer.char = _answer.isCorrect ? item.char.toUpperCase() : '';
      break;
      case 'choose':
        let _choosen2 = -1,
        _cnt = 0;
        for (let secItem of document.querySelectorAll(`#question-card-${_position} [name="choose"]`)) {
          if (secItem.checked)
            _choosen2 = _cnt;
          _cnt++;
        }
        _answer.isCorrect = item.answer[_choosen2].isMe;
        _answer.char = _answer.isCorrect ? item.char.toUpperCase() : '';
      break;
    }
    _answers.push(_answer);
    _position++;
  }
  document.getElementById('modal-check-body').innerHTML = `
    <div class="table-responsive">
      <table class="table table-striped table-sm">
        <thead>
          <tr>
            <th>Вопрос</th>
          </tr>
        </thead>
        <tbody>
          ${(() => {
            let _ret = '',
              _wordCommit = '';
            for (let answer of _answers) {
              if (answer.isCorrect) {
                _wordCommit += `
                  <li class="list-group-item">
                    <span>
                        <strong>${answer.char}</strong>
                    </span>
                  </li>
                `;
                _ret += `
                  <tr>
                    <td class="table-success">${answer.name}</td>
                  </tr>
                `;
              } else {
                _ret += `
                  <tr>
                    <td class="table-danger">${answer.name}</td>
                  </tr>
                `;
                _wordCommit += `
                  <li class="list-group-item">
                    <span>
                        <strong>*</strong>
                    </span>
                  </li>
                `;
              }
            }
            if (_questionsWord.length !== 0)
              document.getElementById('quest-word').innerHTML = _wordCommit;
            return _ret;
          })()}
        </tbody>
      </table>
    </div>
    <a class="btn btn-primary" role="button" href="index.html">🏡 Вернуться на главную</a>
  `;
  let modal = new bootstrap.Modal('#modal-check');
  modal.toggle();
}