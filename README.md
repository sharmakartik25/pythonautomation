# pythonautomation
Python app to run custom commands and scripts on remote hosts

## <font color='blue'>Python Runbook automation task using Flask</font>

#### 1. Flask Setup

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Run the below commands on master 

- sudo apt-get update
- sudo apt-get upgrade
- sudo apt-get install python-dev
- sudo apt-get install python-flask
- sudo apt-get install python-pip
- sudo apt-get install virtualenv
- sudo apt-get install python-virtualenv
- sudo apt-get install python-pip python-dev libffi-dev libssl-dev libxml2-dev libxslt1-dev libjpeg8-dev zlib1g-dev
- pip install paramiko
- mkdir myproject
- cd myproject
- virtualenv venv
- . venv/bin/activate

#### 2. Copy the code in file code.py
#### 3. Copy the key in /home/key.pem on Master

#### 4. Keep the following ready to pass as arguments to rest api:
- Hostname(DNS).
- Username
- RSA-Key
- Commands to be executed on minion machine
    
#### 5. Run Python script 
- python code.py

#### 6 On duplicate terminal of master run the following to post the arguments:
- curl -H "Content-Type: application/json" -X POST -d '{"Arguments": {"id": "13","host": "ec2-35-165-180-52.us-west-2.compute.amazonaws.com","username": "ubuntu","rsa-key": "key.pem","command": ["ls -lts /home/ubuntu", "mkdir /home/ubuntu/test"]}}' http://localhost:5000/messages 

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OR

#### POST Request

METHOD  |  URI                        |DESCRIPTION
--------|---------------------------- |-------------
POST    | /messages                   |connect to remote host and execute command

<p>
It establish connection with given details of host and execute command on it.
</p>

##### <b>Important</b>

<p>
For sending request through request body select raw as a body editor.
</p>

##### <b>Normal response codes</b>: 200

##### <b>Error response codes</b>: 



**Note**
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This table shows the header parameters for post request:</p>

Name                 |  Type                       |DESCRIPTION
---------------------|---------------------------- |-------------
Content-Type         | String                      |application/json



###### JSON request

```
{
"Arguments": {
            "id": "13",
            "host": "ec2-35-165-39-113.us-west-2.compute.amazonaws.com",
            "username": "ubuntu",
            "rsa-key": "key.pem",
            "command": ["ls -lts /home/ubuntu", "mkdir /home/ubuntu/test"]
            }
}

```
