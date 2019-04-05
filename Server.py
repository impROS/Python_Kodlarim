from flask import Flask, jsonify,request
from datetime import datetime
import json
import DQN as DQN
from DQN import Qlearner;
app = Flask(__name__)

done = False
batch_size = 32
EPISODES = 100
agent = "";
input_size = 0;
output_size = 0;
print("DDD");
@app.route('/acc', methods = ['POST','GET']) 
def samplefunction(): # ping deneme
	num = {};
	ping = request.args.get("request") # gelen parametreler
	num["request"] = ping;
	ping = "pong" if ping=="ping" else "request yanlış";
	time = str(datetime.now())
	num["time"] = time;
	num["response"] = ping;
	response = jsonify(num)
	response.headers.add('Access-Control-Allow-Origin', '*')
	print(response);
	return response;


@app.route('/defModel', methods = ['POST','GET'])
def defModel():
	num = {};
	num["input"] = int(request.args.get("input"))
	num["output"] = int(request.args.get("action"))
	global agent
	agent = Qlearner(num["input"], num["output"])
	#agent.load('DosyaYolu'); #num ['input'] ve outputu sil
 	response = jsonify(num)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response;


@app.route('/act', methods = ['POST','GET'])
def act():
	num = {};
	num["rawState"] = request.args.get("state")
	num["state"] = json.loads(num["rawState"])
	print(num["state"])
	num["action"] = DQN.act(agent,num["state"])
	response = jsonify(num)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response;

@app.route('/outCome', methods = ['POST','GET'])
def outCome():
	num = {};
	num["rawoutcome"] = request.args.get("outcome")
	num["outcome"] = json.loads(num["rawoutcome"])
	num["state"]  = num["outcome"]["state"]
	num["next_state"] =num["outcome"]["next_state"]
	num["reward"] = num["outcome"]["reward"]
	num["done"] = num["outcome"]["done"]
	num["action"]  = num["outcome"]["action"]
	DQN.remember(agent,num["state"] , num["action"], num["reward"], num["next_state"], num["done"] )
	response = jsonify(num)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response;
	pass
	

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

yedek_ep = 1;

if __name__ == '__main__':
    port = "80"
    app.run(host='127.0.0.1', port=port)
    #for x in range(1,EPISODES):
		trainmodel(batch_size)
    	#pass
    	yedek_ep = agent.epsilon;
    	agent.epsilon = 0;

  	#agent.save("Dosya");