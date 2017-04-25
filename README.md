# pythonautomation
Python app to run custom commands and scripts on remote hosts

## <font color='blue'>Python Runbook automation task using Flask</font>

#### 1. Docker Setup
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Run the below commands on master:
- sudo apt-get update
- sudo apt-get upgrade
- sudo apt-get install \
  linux-image-extra-$(uname -r) \
  linux-image-extra-virtual
- sudo apt-get install \
  apt-transport-https \
  ca-certificates \
  curl \
  software-properties-common
- curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
- sudo apt-key fingerprint 0EBFCD88
- sudo add-apt-repository \
  "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) \
  stable"
- sudo apt-get update
- apt-get install docker-ce
- mkdir myproject
- cd myproject

#### 2. Git Setup
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Run the below commands on master:
- sudo apt-get update
- sudo apt-get install git

#### 3. Pull the current code from Git to Master & create the configuration
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Run the below commands on master: 
- git clone https://github.com/sharmakartik25/pythonautomation.git

#### 4. Keep the following ready to pass as arguments to rest api
- Hostname(DNS).
- Username
- RSA-Key
- Commands to be executed on minion machine

#### 5. Copy your remote minion private-keys in the cloned key directory
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Run the below commands on master: 
- cp key.pem pythonautomation/key/

#### 6. Build & Run the required container on your master
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Run the below commands on master: 
- cd pythonautomation
- docker build -t pythonautomation .
- docker run -p 4000:5000 dockerapp
- Alternatively you can run the following command to test the pushed container Image directly from Docker Repo

#### 7. As alternate to step 6, run the following command to test the pushed container Image directly from Docker Repo
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Run the below commands on master: 
- docker run -p 4000:5000 sharmakartik25/pythonautomation:flaskapp

#### 6 On duplicate terminal of master run the following to post the arguments
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Run the below commands on master: 
- curl -H "Content-Type: application/json" -X POST -d '{"Arguments": {"id": "1","host": "remote_minion_public_ip/DNS","username": "username_for_remote_minion","rsa-key": "name_of_the_key_file_used","command": ["ls -ltr /home/ubuntu", "mkdir /home/ubuntu/test"]}}' http://remote_minion_public_ip/DNS:4000/api/run/

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OR

#### POST Request

METHOD  |  URI                        |DESCRIPTION
--------|---------------------------- |-------------
POST    | /api/run/                   |connect to remote host and execute command

<p>
It establish connection with given details of host and execute command on it.
</p>

##### <b>Important</b>

<p>
For sending request through request body select raw as a body editor.
</p>

##### <b>Normal response codes</b>: 200

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
            "host": "remote_minion_public_ip/DNS",
            "username": "username_for_remote_minion",
            "rsa-key": "name_of_the_key_file_used",
            "command": ["ls -lts /home/ubuntu", "mkdir /home/ubuntu/test"]
            }
}
```
#### GET Request

METHOD  |  URI                        |DESCRIPTION
--------|---------------------------- |-------------
GET     | /api/run/                   |connect to remote host and execute command

<p>
For testing the app working.
</p>

##### <b>Normal response codes</b>: 200

**Note**
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This table shows the header parameters for get request:</p>

Name                 |  Type                       |DESCRIPTION
---------------------|---------------------------- |-------------
Content-Type         | String                      |application/json
