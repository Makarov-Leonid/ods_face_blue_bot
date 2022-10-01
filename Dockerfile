# сообщает нам на каком образе будет построен наш образ
FROM python:3.10
# задаем рабочую директорию
WORKDIR /app
# копируем все остальные файлы нашего приложения в рабочую директорию
COPY . /app
# запускаем команду которая установит все зависимости для нашего проекта
RUN pip install -r /app/requirements.txt
RUN pip install git+https://github.com/rcmalli/keras-vggface.git
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
# заупскаем наше приложение
CMD python /app/bot.py