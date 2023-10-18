   This Project is developed for studying purpose only.
Its aim is to show the author hand-on skills only, so it is implemented from the perspective
to show different methods and cover next requirements:

1. Створити зручну для підтримки проєкту структуру модулів та пакунків.    
    * модуль -- файл .py
    * пакунок -- тека з файлом __init__.py
 _____________DONE
 _____________COMMENT: Tests_Search_with_Filters -> test_global_search_wallart implemented without pageObject
 other UI tests implemented with with pageObject or partially with PageObject.
 API tests located separately from UI tests due to difference in fixture usage


2. Зробити пакунок для тестів, в якому тести різного типу будуть логічно розміщені
______________COMMENT: not clear requirement.

3. Обов'язково використовувати фікстури. Бажано застосувати в тестах фікстури
    з різними scope (наприклад 'module', 'session', 'class').
______________PARTIALLY DONE
______________COMMENT: Only "package" scope is implemented, as "session" unnecessary for API tests,
other levels were not required by tests context.

    * Тримайте фікстури в спеціально визначених для цього місцях (conftest.py)
______________DONE

4. Оберіть ресурси (сайти, API) для тестування на свій смак
______________DONE

5. Створіть 5 UI тестів (selenium)
______________DONE
______________COMMENT: test_upload, test_buyer_login, test_redirection_to_registration, test_global_search,
test_filter_search

та 5 API тестів (requests) -> test_api_buyer_login,
______________UNCOMPLETED: 1 valid test, 4 invalid !!!!!!!!!!!
______________COMMENT: https://petstore.swagger.io/#/pet/findPetsByStatus

* Бажано щоб тести покривали різні аспекти роботи:
** selenium: робота з різними типами елементів (чекбокс, випадаючий список і т.п.)
______________COMMENT: checkbox, text field, file upload field, buttons, links

** requests: робота з різними типами запитів (get, post, put, delete)
______________COMMENT: POST, GET, DELETE, PUT


6. Передбачте можливість вибіркового запуску тестів за мітками (pytest.mark)
______________DONE
______________COMMENT: pytest.ini file -> regression, smoke, used test_global_search randomly

!!!
В проєкті мають обов'язково бути файли:
   .gitignore -- зі списком файлів/тек які ми не пушимо в репозиторій
 ______________DONE

   requirements.txt -- зі списком необхідних залежностей
 ______________DONE

   README.md -- із загальним описом проєкту, можливо якихось особливостей
  ______________DONE

   pytest.ini
 ______________DONE

 ;)


