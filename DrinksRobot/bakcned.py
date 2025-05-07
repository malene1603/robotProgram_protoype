from flask import Flask, request, jsonify
from flask_cors import CORS

from ScriptQueue import ScriptQueue
from DrinksProgrammer import DrinksProgrammer
from RobotComms import RobotComms
from RobotState import RobotState


progress_counter = {"done": 0, "total": 1}
app = Flask(__name__)
CORS(app)

# Robotforbindelser
robot_connection = RobotComms("192.168.0.101")
script_queue = ScriptQueue(robot_connection)
programmer = DrinksProgrammer(robot_connection, script_queue)

@app.route('/run_drink', methods=['POST'])
def run_drink():
    data = request.get_json()
    print(f"Modtaget data: {data}")

    if 'ingredients' in data:
        ingredients = data['ingredients']
        print(f"Mix Selv valgt: {ingredients}")
        programmer.mix_drink(ingredients)
        return "Mix Selv drink startet!", 200

    elif 'drink' in data:
        drink = data['drink']
        print(f"Færdig drink valgt: {drink}")
        programmer.run_program(drink)
        return "Færdig drink startet!", 200

    else:
        return "Forkert data sendt!", 400

@app.route('/robot_status', methods=['GET'])
def robot_status():
    is_running = robot_connection.is_program_running()
    return {
        "running": is_running,
        "progress": RobotState.progress_done,
        "total": RobotState.progress_total,
        "current_program": RobotState.current_program_name  # ← send med
    }, 200

@app.route('/robot_progress', methods=['GET'])
def robot_progress():
    return {
        "done": RobotState.progress_done,
        "total": RobotState.progress_total
    }, 200

@app.route('/current_program', methods=['GET'])
def get_current_program():
    name = RobotState.current_program_name
    return jsonify({"program": name})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
