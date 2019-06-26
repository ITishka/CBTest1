# – FILE: features/some.feature # language: ru
Feature: Test example

  Background:
    Given пользователь на странице "https://www.google.ru/"

 Scenario: Сheck habr
    Then очистили среду
    Then отображается поле "Поиск"
    Then ввели в поле "q" "хабр"
    Then дождались загрузки страницы "resultStats"
    When нажали на ссылку "Лучшие публикации за сутки / Хабр"
    When нажали на ссылку "Регистрация"
    Then дождались загрузки страницы "register_form"
    Then ввели в поле "email" "хабр"
    Then вышло сообщение "Введите корректный e-mail"
    When сняли чек-бокс "Я принимаю условия"
    Then вышло сообщение "Необходимо принять пользовательское соглашение"
    When сделали скриншот
    When нажали на ссылку "Обратная связь"
    Then выбрали из списка "Гениальная идея"
    When запомнили текст из элемента "shadow-box__title"
    When нажали на ссылку "English"
    When запомнили текст из элемента "shadow-box__title"
    Then сравнили запомненные текст1 и текст2
    When сделали скриншот
    When закончили тест

