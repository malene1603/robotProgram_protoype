from flask import Flask, request
from flask_cors import CORS

from ScriptQueue import ScriptQueue
from DrinksProgrammer import DrinksProgrammer
from RobotComms import RobotComms

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
    return {"running": is_running}, 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
