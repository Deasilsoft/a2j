# deasilsoft/a2j

A JSON API analyzing Age of Empires II records.

[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/Deasilsoft/a2j.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Deasilsoft/a2j/context:python)
[![CodeFactor](https://www.codefactor.io/repository/github/deasilsoft/a2j/badge)](https://www.codefactor.io/repository/github/deasilsoft/a2j)
![Code Inspector Grade](https://www.code-inspector.com/project/25065/status/svg)

## Setup

### Using Docker

1. Pull the image from Docker Hub.

       docker pull deasilsoft/a2j:latest

2. Run container with the image and publish the port.

       docker run -p 8080:8080 deasilsoft/a2j

### Using pip

TODO: Add instructions how to install using pip.

### Direct Download

1. Download the repository from Github.

2. Navigate to the project root directory.

3. Run with docker-compose.

        docker-compose up --build -d

## Usage

This is an API ran as a Docker container. Mount to the `records` directory to add and remove records from the API.

### Endpoints (TODO: change to RESTFUL)

    localhost:8080/a2j/
    localhost:8080/a2j/v1/
    localhost:8080/a2j/v1/parse/
    localhost:8080/a2j/v1/clean/

There is a list of endpoints available from `localhost:8080/a2j/v1/parse/` which are available in the `endpoints`
array. These endpoints can be added recursively to retrieve the data you desire.

By adding the `record` argument you select the Age of Empires II record to parse or to clean.

## Examples

### Parse

This example will retrieve all the `teams` and `players` from the `test.mgz` record.

    curl localhost:8080/a2j/v1/parse/teams/players/?record=test.mgz

The output is a JSON object.

### Clean

To clean all cached data from a record you can do the following.

    curl localhost:8080/a2j/v1/clean/?record=test.mgz

This is useful in cases where you replace a record and want to generate a new cache hierarchy for the new data.
