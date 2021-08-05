# deasilsoft/a2j

A RESTFUL JSON API for analyzing Age of Empires II records.

[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/Deasilsoft/a2j.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Deasilsoft/a2j/context:python)
[![CodeFactor](https://www.codefactor.io/repository/github/deasilsoft/a2j/badge)](https://www.codefactor.io/repository/github/deasilsoft/a2j)
[![Code Inspector Grade](https://www.code-inspector.com/project/25065/score/svg)](https://frontend.code-inspector.com/project/25065/dashboard)

## Setup

### Add To Your Docker Compose Project (Recommended)

1. Create an **.env** file with values from **.env.example** from this project (or append to existing file):

   Replace `FLASK_ENV=development` with `FLASK_ENV=production` for production.

2. Add this **service** to your **docker-compose.yml** file:

       a2j:
         # Build from image
         build: deasilsoft/a2j

         # Load environment variables
         env_file:
           - .env

         # Remove ports in production
         ports:
           - "${A2J_HOST_PORT}:8080"

         # Bind to local directory
         volumes:
           - "./records:${A2J_HOME}/records"

         # Always restart container on Docker start
         restart: always

   Remove **ports** for production and access the API with `curl YOUR_PROJECT_a2j_1:8080` instead.

### Direct Download & Docker Compose

1. Download the repository from Github with and open project root:

       git clone https://github.com/Deasilsoft/a2j.git
       cd a2j

3. Copy **.env.example** to **.env** with `cp .env.example .env` and make changes to **.env** as you desire.

4. Make changes to **docker-compose.yml** as you desire.

5. Run the Docker container with:

       docker compose up --build -d

### Using Only Docker

1. Pull the image from Docker Hub with:

       docker pull deasilsoft/a2j:latest

3. Run the Docker container with:

   #### For Development:

       docker run -d --name a2j --env FLASK_ENV=development -p 8080:8080 -v ABSOLUTE_PATH_TO_RECORDS:/home/a2j/records deasilsoft/a2j:latest

   #### For Production:

       docker run -d --name a2j --env FLASK_ENV=production -v ABSOLUTE_PATH_TO_RECORDS:/home/a2j/records --restart always deasilsoft/a2j:latest

*Remember to replace **ABSOLUTE_PATH_TO_RECORDS** with your value.*

Read more about the [`docker run`](https://docs.docker.com/engine/reference/commandline/run/) syntax.

### Using pip

Instructions are pending...

## Usage

This is a RESTFUL API ran as a Docker container behind a secure firewall. Mount to the `records` directory to add and remove records from the API.

### Endpoints

    localhost:8080/
    localhost:8080/minimap/<record>/ (W.I.P.)
    localhost:8080/record/<record>/<commands...>/

A list of `endpoints` is available from `localhost:8080/record/<record>/<commands...>/`. These `endpoints` can be added recursively to the path in order to retrieve the data you
desire.

## Examples

### GET

This example will retrieve a JSON object of all the `teams` and `players` from the `test.mgz` record.

    curl localhost:8080/record/test.mgz/teams/players/

### DELETE

To delete all cached data from a `record` you can do the following.

    curl -X DELETE localhost:8080/record/test.mgz/

This is useful in cases where you replace a `record` and want to generate a new cache, or for a general cleanup. Generally, you don't want to remove cached data unless the `record`
has changed.
