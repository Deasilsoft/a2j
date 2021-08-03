# deasilsoft/a2j

A JSON API analyzing Age of Empires II records.

[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/Deasilsoft/a2j.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Deasilsoft/a2j/context:python)
[![CodeFactor](https://www.codefactor.io/repository/github/deasilsoft/a2j/badge)](https://www.codefactor.io/repository/github/deasilsoft/a2j)
![Code Inspector Grade](https://www.code-inspector.com/project/25065/status/svg)

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

There is a list of endpoints available from `localhost:8080/a2j/v1/parse/` which are available in the `endpoints`
array. These endpoints can be added recursively to retrieve the data you desire.

By adding the `record` argument you select the Age of Empires II record to parse or to clean.

## Examples

### Parse

This example will retrieve all the `teams` and `players` from the `test.mgz` record.

    curl localhost:8080/record/test.mgz/teams/players/

The output is a JSON object.

### Clean

To clean all cached data from a record you can do the following.

    curl localhost:8080/record/test.mgz/clean/

This is useful in cases where you replace a record and want to generate a new cache hierarchy for the new data.
