# W4153-P1-Application

Simple microservice application for the first project in W4153 -- Cloud Computing.

## Running locally
1. Clone the repo using: <code>git clone https://github.com/dwr2118/W4153-Team6-Project-UserApp.git</code> on your machine.
2. Ensure that python is installed on your machine by doing <code>python3 --version</code> or <code>python --version</code>.
3. Create and enable a python virtual environment on your machine whether it be local or a virtual machine on GCP.
4. Download all the necessary packages using: <code>pip install -r requirements.txt</code>.
5. Grab the MySQL password from the WhatsApp group chat and run <code>EXPORT DBPASSWORD="<INSERT PASSWORD FROM DB>"</code>. TODO: fix this 
6. Now ensure you have the correct public IP address to the MySQL database held in GCP by running the test method from within the root folder of the repo: <code>python3 -m pymysql</code>. This should return a json object like such: "". TODO: fill this in.
