# driver_tiktok_tz

Это тестовое задание для проекта "Тикток для водителей". Здесь реализована веб-страница с картой, на которой можно добавлять и удалять метки. 

Для запуска нужно запустить back.py на 127.0.0.1:4351 и front.py на 127.0.0.1:5000. Рекомендуется запустить скрин:

$ screen -S back

На нем при помощи uvicorn запустить back:

$ uvicorn back:app --reload --port 4351

После этого выйти из скрина при помощи Ctrl+d и запустить front:

$ export FLASK_APP=front
$ export FLASK_ENV=development
$ flask run --reload

Затем открыть 127.0.0.1:5000/home в браузере (поддерживаются Opera и Chrome). 
