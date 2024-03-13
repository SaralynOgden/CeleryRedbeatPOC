from flask import Flask, Response
from flask import jsonify
from redbeat import RedBeatSchedulerEntry
from worker import celery_app

import celery.states as states

dev_mode = True
app = Flask(__name__)

@app.route('/add/<int:param1>/<int:param2>')
def add(param1: int, param2: int) -> str:
    schedule_name = '{} + {}'.format(param1, param2)
    entry = RedBeatSchedulerEntry(
        schedule_name,
        'tasks.add',
        30,
        args=[param1, param2],
        kwargs={"schedule_name": schedule_name},
        app=celery_app
    )
    entry.save()
    return "Adding!"

@app.route('/addSchedule/<string:symbol_name>')
def addSchedule(symbol_name: str) -> str:
    entry = RedBeatSchedulerEntry(
        symbol_name,
        'tasks.check_for_trade',
        30,
        args=[symbol_name],
        kwargs={"schedule_name": symbol_name},
        app=celery_app
    )
    entry.save()
    return "Schedule created"


@app.route('/check/<string:task_id>')
def check_task(task_id: str) -> str:
    res = celery_app.AsyncResult(task_id)
    if res.state == states.PENDING:
        return res.state
    else:
        return str(res.result)


@app.route('/health_check')
def health_check() -> Response:
    return jsonify("OK")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
