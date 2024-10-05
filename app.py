from flask import Flask, render_template, request, jsonify
import threading, time
from datetime import datetime

app = Flask(__name__)
log_lock = threading.Lock()
output_log = []


def log_message(message):

    with log_lock:

        output_log.append(f" - {message}")
        print(f" - {message}")


def add_delay_and_log(message, delay):

    log_message(message)
    time.sleep(delay)


def start_washing_cycle():
    log_message("Пральна машинка запускається. прання продовжиться 64 сек")

    add_delay_and_log("Немає миючого засобу. Додайте миючий засіб (подовжиться 2 сек", 2)
    add_delay_and_log("Миючий засіб додано.", 0)

    add_delay_and_log("Барабан порожній. Зввантажте брудний білизну (продовжиться 4 сек )", 4)
    add_delay_and_log("Білизну завантажено.", 0)

    add_delay_and_log("Вид прання не задано. Виберіть вид прання (продовжиться 3 сек)", 3)
    add_delay_and_log("Вид прання задано.", 0)

    add_delay_and_log("Натисніть кнопку ПУСК для початку прання (продовжиться 1 сек)", 1)
    add_delay_and_log("Машинку запущено.", 0)


    add_delay_and_log("Немє води,Вода набирається (продовжиться 15 сек)", 10)
    add_delay_and_log("Воду набрано.", 0)

    add_delay_and_log("Вода холона, Йде нагрівання води (продовжиться 10 сек)", 10)
    add_delay_and_log("Воду нагріто.", 0)

    add_delay_and_log("Машинка починає розкручуватись (продовжиться 25 сек)", 10)
    add_delay_and_log("Білизну викручено.", 0)

    add_delay_and_log("Вивід брудної води (продовжиться 5 сек)", 5)
    add_delay_and_log("Брудну воду виведено.", 0)

    add_delay_and_log("Чиста вода для полоскання набирається (продовжиться 5 сек)", 10)
    add_delay_and_log("Чисту воду набрано.", 0)

    add_delay_and_log("Білизна полощеться (продовжиться 15 сек)", 5)
    add_delay_and_log("Білизна виполоскано.", 0)

    add_delay_and_log("Вивід брудної води (продовжиться 5 сек)", 5)
    add_delay_and_log("Брудну воду виведено.", 0)

    add_delay_and_log("Машинка починає розкручуватись (продовжиться 25 сек)", 10)
    add_delay_and_log("Одяг викручується.", 0)

    add_delay_and_log("Йде сушка одягу (продовжиться 5 сек)", 5)
    add_delay_and_log("Одяг висушено", 0)

    add_delay_and_log("Відкрийте машинку та  не забудьте забрати одяг (продовжиться 5 сек)", 5)
    add_delay_and_log("Машина готова до використання.", 0)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        log_message("Початок нового циклу.")
        thread = threading.Thread(target=start_washing_cycle)
        thread.start()
        return render_template('index.html', result=output_log)

    return render_template('index.html', result=None)


@app.route('/output_log')
def fetch_log():

    with log_lock:
        return jsonify(output_log)


if __name__ == '__main__':
    app.run(debug=True)
