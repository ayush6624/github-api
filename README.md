# Github API Wrapper   
[![Build Status](https://travis-ci.com/ayush6624/github-api.svg?token=ZNZvRCTh5oMvBSaJxVvJ&branch=master)](https://travis-ci.com/ayush6624/github-api)   
## This is a Github API wrapper with custom endpoints

API can be reached at https://api.goyal.club

## Docker Container Setup
The API can also be built and run as a Docker container:
```bash
docker build -t github-api .
docker run -it -p 5000:5000 --name github-custom-api github-api
```

## Local Installation Setup
```bash
pip3 install -r requirements.txt
python3 app.py
```
## Endpoints
`/contributor/{repository-owner}/{repository-name}`

Returns the list of the Top 5 Contibutors of any repository with their Github Username, Number of Contributions and a link to their Github Profile.

If either of the above parameters is missing, a `404` error is returned.
If incorrect endpoint is requested, a `400` error is returned.
___

`/popular`

Returns the top 3 popular repositories of 3 languages - `Kotlin`, `Ruby` and `Go`.   
Each contains the Full Name Of The Repo, Repository Description, language, and the number of stars.
___

`/apidocs`

Front-End To Test the API
___

## Description

- This project uses `flake8` linting guidelines.   
- The API is hosted on AWS ap-south-1 (Mumbai Region) on a serverless function through Zeit Now Serverless Platform.   
- Each Commit and PR was deployed as a separate function to rule out any errors.   
- Unit-testing is implemented which checks for `flake8` guidelines enforcement, and if the API is working as desired by checking the status repsonse codes for different endpoints using Travis-CI   

- I used the `Flask` framework to quickly build the API.   
- I also used the `flasgger` library to Build a Front-end For the API (Got the idea from my previous project)   
- Flasgger uses the `Swagger UI` To quickly build the UI by specifying the configuration in `YAML` format under the function name as a comment (Very Similar To a Docstring).   
- The UI can be reached at `/apidocs`. Click on the `Try It Out` Button, and enter the value of parameters (if required)    
- **Note**: I could have used the `@swag_from` to link to an external `YAML` file, but for the sake of simplicity, and to modify the UI easily, I included the configuration in the Python file itself.   