# deasilsoft/a2j

A RESTFUL JSON API for analyzing Age of Empires II records.

[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/Deasilsoft/a2j.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Deasilsoft/a2j/context:python)
[![CodeFactor](https://www.codefactor.io/repository/github/deasilsoft/a2j/badge)](https://www.codefactor.io/repository/github/deasilsoft/a2j)
[![Code Inspector Grade](https://www.code-inspector.com/project/25065/score/svg)](https://frontend.code-inspector.com/project/25065/dashboard)

## Setup

### Using Docker

1. Pull the image from Docker Hub with `docker pull deasilsoft/a2j:latest`.

2. Copy `.env.example` to `.env` with `cp .env.example .env` and replace values to your desired values within `.env`.

3. Run the Docker container and publish the port with `docker run --env-file ./.env -p 8080:8080 deasilsoft/a2j`.

### Using pip

Instructions are pending...

### Direct Download

1. Download the repository from Github with `git clone https://github.com/Deasilsoft/a2j.git`.

2. Navigate to the project root directory with `cd a2j`.

2. Copy `.env.example` to `.env` with `cp .env.example .env` and replace values to your desired values within `.env`.

3. Run the Docker container with `docker compose up --build -d`.

## Usage

This is an API ran as a Docker container. Mount to the `records` directory to add and remove records from the API.

### Endpoints

    localhost:8080/
    localhost:8080/minimap/<record>/
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
