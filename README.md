# Assignment 1 - Data exploration tool

[![Deploy on EC2](https://github.com/BigDataIA-Spring2023-Team-05/Assignment-01/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/BigDataIA-Spring2023-Team-05/Assignment-01/actions/workflows/main.yml)

## Workflow
<img src="https://github.com/BigDataIA-Spring2023-Team-05/Assignment-01/raw/main/imgpsh_mobile_save.jpg"></img>

Codelabs link:
https://codelabs-preview.appspot.com/?file_id=1--Cgwvu9yb01IJHlHtsJatirkVIYRdJGBXARmGvIq-I#0


## ER Diagram

ER Diagram for the SQL database tables - GOES metadata and NEXRAD metadata - which is storing the data for GOES and NEXRAD metadata.

<img src="https://github.com/BigDataIA-Spring2023-Team-05/Assignment-01/blob/main/ERdiagram.drawio.png"></img>

------------



## How to run this project:
1. Clone this repo locally `git clone <repo-url>`

2. Setup the local python enviornment.

3. Install all the dependencies from the requirements.txt file
`pip install -r requirements.txt`

4. Install all local dependencies 
`pip install -e .`

5. Create `.env` file under awscloud folder

6. Run the streamlit project
`streamlit run ui/main.py`
