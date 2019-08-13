# Программа для публикации комиксов xkcd во вКонтакте

Программа скачивает случайный комикс [xkcd.com](https://xkcd.com) и загружает его в ваш паблик во вКонтакте.

### Как установить

Залогиньтесь в ваш аккаунт [вКонтакте](https://vk.com).
Создайте приложение с типом standalone во [вКонтакте](https://vk.com/dev), перейдя во вкладку "Мои приложения"/"Создать приложение".
Получите `client_id` приложения, нажав "Редактировать" на странице вашего приложения. Спрячьте его в файл .env вот так: `XKCD_CLIENT_ID=7090448`
Получите ключ доступа пользователя, используя процедуру [Implicit Flow](https://vk.com/dev/implicit_flow_user). Запрос должен выглядеть так: [https://oauth.vk.com/authorize?client_id=7090448&display=page&scope=photos,groups,wall,offline&response_type=token&v=5.101&state=123456](https://oauth.vk.com/authorize?client_id=7090448&display=page&scope=photos,groups,wall,offline&response_type=token&v=5.101&state=123456). Подставьте сюда свои client_id и текущую версию api вКонтакте в параметр `v` и скопируйте в строку поиска вашего браузера.

На новом экране подтвердите для приложения доступ к запрашиваемым параметрам.
Вы получите новую ссылку в окне браузера с ключом пользователя: 
[https://oauth.vk.com/blank.html#access_token=aa2b4f6v970017fc775ef4c960655cb82a6c020499a54b3451d04f07dd91и56ec755fb51d2c784333c2ef&expires_in=0&user_id=246785&state=123456](https://oauth.vk.com/blank.html#access_token=aa2b4f6v970017fc775ef4c960655cb82a6c020499a54b3451d04f07dd91и56ec755fb51d2c784333c2ef&expires_in=0&user_id=246785&state=123456). Скопируйте access_token и спрячте его в .env вот так: `VK_IMPLICIT_FLOW_TOKEN=aa2b4f6v970017fc775ef4c960655cb82a6c020499a54b3451d04f07dd91и56ec755fb51d2c784333c2ef`

Получите group_id вашей группы вКонтакте. Для этого скопируйте ссылку на вашу группу из строки браузера и используйте ее здесь:[http://regvk.com/id/](http://regvk.com/id/). Получившийся номер поместите в файл .env вот так: `XKCD_GROUP_ID=-195514543`. Обратите внимание на знак минус!

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Как использовать

`$ python3 main.py`

Пост будет опубликован в паблике. Картинки на ПК не сохраняются.

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).