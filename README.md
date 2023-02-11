# Assignment 1 - Data exploration tool

[![Deploy on EC2](https://github.com/BigDataIA-Spring2023-Team-05/Assignment-01/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/BigDataIA-Spring2023-Team-05/Assignment-01/actions/workflows/main.yml)

WE ATTEST THAT WE HAVEN’T USED ANY OTHER STUDENTS’ WORK IN OUR ASSIGNMENT AND ABIDE BY THE POLICIES LISTED IN THE STUDENT HANDBOOK

### Directory layout
    .
    ├── awscloud             # All the files related to AWS functionality, which connects with S3 and Cloudwatch
    ├── data                # This dir consists of data reelated file (SQLlite)
    ├── grea_expectation    # Great Expecattion
    ├── test                # Automated tests
    ├── ui                  # All the UI Streamlit components
    ├── utils               # Utility functions like logger and status checker.
    └── README.md

#### Automated tests
Automated tests are usually placed into the `test`.

    .
    ├── ...
    ├── test                           # Test files
    │   ├── test_aws_goes.py           # Test cases related to GOES Dataset
    │   └── test_aws_nextrad.py        # Test cases related to NexRad Dataset
    └── ...

#### Automated tests
Automated tests are usually placed into the `test`.

    .
    ├── ...
    ├── awsclooud                           # Test files
    │   ├── cloudwatch   # Code related to Cloudwatch
    │   └── s3           # Code related to S3
    └── ...


### Workflow
<img src="https://github.com/BigDataIA-Spring2023-Team-05/Assignment-01/raw/main/imgpsh_mobile_save.jpg"></img>

Codelabs link:
https://codelabs-preview.appspot.com/?file_id=1--Cgwvu9yb01IJHlHtsJatirkVIYRdJGBXARmGvIq-I#0


### ER Diagram

ER Diagram for the SQL database tables - GOES metadata and NEXRAD metadata - which is storing the data for GOES and NEXRAD metadata.

<img src="https://github.com/BigDataIA-Spring2023-Team-05/Assignment-01/blob/main/ERdiagram.drawio.png"></img>

## How to run this project:
1. Clone this repo locally `git clone <repo-url>`

2. Setup the local python enviornment. You can refer this link [How to setup python enviornment?](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/ "How to setup python enviornment?")

3. Install all the dependencies from the requirements.txt file
`pip install -r requirements.txt`

4. Install all local dependencies 
`pip install -e .`

5. Create `.env` file under awscloud folder

6. Specify these key and values pair in your .env

`AWS_ACCESS_KEY=<value>`

`AWS_ACCESS_KEY_SECRET=<value>`

`TARGET_BUCKET_NAME=<value>` # Target bucket name for GOES in S3 Bucket.

8. Run the streamlit project
`streamlit run ui/main.py`
