from flask import json
from flask import Flask, jsonify
import subprocess
from flask import request
import ast
import paramiko
import os

app = Flask(__name__)

@app.route('/api/run/', methods = ['POST'])
def api_message():

    if request.headers['Content-Type'] == 'application/json':
        sort(request.json)
        return "POST Request Successful !!"

    else:
        return "415 Unsupported Media Type"

def sort(tempobj):
    test=ast.literal_eval(json.dumps(tempobj))
    id = test['Arguments']['id']
    host = test['Arguments']['host']
    username = test['Arguments']['username']
    rsa_key = test['Arguments']['rsa-key']
    commands = test['Arguments']['command']
    remote_connect(commands,id,host,username,rsa_key)
    return "true"


def remote_connect(commands,id,host,username,rsa_key):
    k = paramiko.RSAKey.from_private_key_file("/home/"+rsa_key)
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print "connecting"
    c.connect( hostname=host,username=username,pkey=k )
    print "connected"
    print commands
    for command in commands:
            print "Executing {}".format( command )
            stdin , stdout, stderr = c.exec_command(command)
            print stdout.read()
            print stderr.read()
    c.close()

@app.route('/api/run/', methods = ['GET'])
def get_message():
   return "GET Request Successful !!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
