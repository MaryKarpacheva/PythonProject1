import pytest
from selene import browser, have, by
def test_2():
    browser.open('https://school.qa.guru')
    browser.element('[name="email"]').type('qagurubot@gmail.com')
    browser.element('[name="password"]').type('somepasshere').press_enter()
    browser.element('[class="page-header"]').should(have.text('Список тренингов'))
    browser.open('https://school.qa.guru/cms/system/login')
    browser.element('.logined-form').should(have.text('QA_GURU_BOT'))
