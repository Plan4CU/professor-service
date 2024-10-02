# W4153-P1-Application

Simple microservice application for the first project in W4153 -- Cloud Computing.

## Running locally
1. Clone the repo using: <code>git clone https://github.com/Plan4CU/Plan4CU-ProfessorScrape.git</code> on your machine.
2. Ensure that python is installed on your machine by doing <code>python3 --version</code> or <code>python --version</code>.
3. Create and enable a python virtual environment on your machine whether it be local or a virtual machine on GCP.
4. Download all the necessary packages using: <code>pip install -r requirements.txt</code>.
5. Now ensure you have the correct public IP address to the MySQL database held in GCP by running the test method from within the root folder of the repo: <code>python3 -m tests.tmysqldb</code>. This should return a json object like such: 
```json
 {
    "course_id": 204283,
    "course_name": "COMSW4153_001_2024_3 - Cloud Computing",
    "uuid": "3jHCxUV0ck9Z8TF1sZeI8WTx47olDGkX1YPL3USM",
    "created_at": "024-04-05T00:58:50Z",
    "course_code": "COMSW4153_001_2024_3 - Cloud Computing",
    "sis_course_id": "COMSW4153_001_2024_3",
    "course_no": "COMSW4153",
    "section": "001",
    "course_year": "2024",
    "semester": "3"
}
```
