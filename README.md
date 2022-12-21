# Deasilsoft/a2j

A Restful JSON API as a service for analyzing Age of Empires II records.

[![Code Tests](https://img.shields.io/github/actions/workflow/status/Deasilsoft/a2j/.github/workflows/tests.yaml?branch=main&label=pytest&logo=pytest&logoWidth=18)](https://github.com/Deasilsoft/a2j/actions/workflows/tests.yaml)
[![Codecov Coverage](https://img.shields.io/codecov/c/github/deasilsoft/a2j?logo=codecov&logoWidth=18)](https://app.codecov.io/gh/Deasilsoft/a2j)
[![Codiga Score](https://api.codiga.io/project/25065/score/svg)](https://app.codiga.io/public/project/25065/a2j/dashboard)
[![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/deasilsoft/a2j/main?label=CodeFactor&logo=codefactor&logoWidth=18)](https://www.codefactor.io/repository/github/deasilsoft/a2j)
[![LGTM Alerts](https://img.shields.io/lgtm/alerts/github/Deasilsoft/a2j?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Deasilsoft/a2j/context:python)  
[![Docker Build](https://img.shields.io/github/actions/workflow/status/Deasilsoft/a2j/.github/workflows/docker-hub.yaml?branch=main&logo=docker&logoWidth=18)](https://github.com/Deasilsoft/a2j/actions/workflows/docker-hub.yaml)
[![Docker Image Size](https://img.shields.io/docker/image-size/deasilsoft/a2j?logo=docker&logoWidth=18)](https://hub.docker.com/r/deasilsoft/a2j)
[![Docker Pulls](https://img.shields.io/docker/pulls/deasilsoft/a2j?logo=docker&logoWidth=18)](https://hub.docker.com/r/deasilsoft/a2j)
[![Docker Stars](https://img.shields.io/docker/stars/deasilsoft/a2j?logo=docker&logoWidth=18)](https://hub.docker.com/r/deasilsoft/a2j)  
[![Github Watchers](https://img.shields.io/github/watchers/deasilsoft/a2j?logo=github&logoWidth=18)](https://github.com/Deasilsoft/a2j/watchers)
[![Github Stars](https://img.shields.io/github/stars/deasilsoft/a2j?logo=github&logoWidth=18)](https://github.com/Deasilsoft/a2j/stargazers)
[![Github Forks](https://img.shields.io/github/forks/deasilsoft/a2j?logo=github&logoWidth=18)](https://github.com/Deasilsoft/a2j/network/members)
[![Github Issues](https://img.shields.io/github/issues-raw/deasilsoft/a2j?logo=github&logoWidth=18)](https://github.com/Deasilsoft/a2j/issues)
[![Github Contributors](https://img.shields.io/github/contributors/deasilsoft/a2j?logo=github&logoWidth=18)](https://github.com/Deasilsoft/a2j/pulls)
[![Github Commits](https://img.shields.io/github/last-commit/deasilsoft/a2j?logo=github&logoWidth=18)](https://github.com/Deasilsoft/a2j/commits/main)

---

## Installation

### Add To Your Docker Compose Project (Recommended)

1. Copy the `production` service found in `docker-compose.yml` to your project.

Delete `test.mgz` and `corrupt.aoe2record` from the `records` directory.

### Direct Download & Docker Compose (Development)

1. Clone Deasilsoft/a2j and open the project directory with `git clone https://github.com/Deasilsoft/a2j.git && cd a2j`
2. Make changes to **docker-compose.yml** as you desire.
3. Run the Docker container(s) with `docker-compose up --build -d`

#### Tips & Tricks for Development

* `python ./tests/data/prettier.py` to prettify `match.json` and `summary.json`.
* Run tests locally with `docker-compose exec -T development pytest --cov=src --cov-report=xml tests`

### Using Only Docker (Production)

1. Pull the image from Docker Hub with `docker pull deasilsoft/a2j:latest`
2. Run the Docker container with `docker run -d --name a2j -v ABSOLUTE_PATH_TO_RECORDS:/home/a2j/records --restart always deasilsoft/a2j:latest`

Delete `test.mgz` and `corrupt.aoe2record` from the `records` directory.

*Remember to replace **ABSOLUTE_PATH_TO_RECORDS** with your own value.*

Read more about the [docker run syntax](https://docs.docker.com/engine/reference/commandline/run/).

---

## Usage

This is a Restful API running in a Docker container preferably **behind your secure firewall** (security requirement). This service should not be accessible from `localhost:5000`
(or any other port). This is built as a service specifically to make it possible to be used with any tech stack, in particular websites not necessarily running with Python. This
service is perfect for websites built with PHP.

You can add more record files from the host by placing the record files inside the directory named `records` in the project directory. The purpose of the API is to easily and
efficiently retrieve the data you want from an Age of Empires II record file. The output data is JSON, which is easy to handle in any programming language. The JSON data is cached
to increase speed and reduce usage of your valuable computing power.

### Endpoints

Path and query parameters within `<>` or `[]` brackets are dynamic values. `<>` are required, and `[]` are optional. Optional values have default values, which are given after
the `|` separator. ***Example** `[optional=foo,bar|bar]` allows `foo` and `bar` as valid values, but `bar` is the default value if no value is supplied.*

    container_name:5000/
    container_name:5000/minimap/<record>/?[scale=1-15|5]
    container_name:5000/record/<record>/<commands...>/?[method=summary,match|summary]

Whenever you get a list of `endpoints` from a request, you can add one of them at the end of your current path (before query parameters).

---

## Examples

Below are some examples of usage. These examples use `curl` as a tool to send requests, any other means of sending requests will work as well. `container_name` is an example name
of the Docker container running Deasilsoft/a2j. We strongly recommend naming the container a2j and **NOT** publishing the port.

### GET

#### Record Data

This example will retrieve a JSON object of all the `teams` and `players` from the `test.mgz` record.

    curl container_name:5000/record/test.mgz/teams/players/

This example will retrieve a JSON object of all the `actions` from the `test.mgz` record.

    curl container_name:5000/record/test.mgz/actions/?method=match

#### Minimap

This example will retrieve a PNG image with our interpretation of the Age of Empires II minimap.

    curl container_name:5000/minimap/test.mgz/

### DELETE

#### Cached Data

To delete all *cached data* from a record file you can do the following.

    curl -X DELETE container_name:5000/record/test.mgz/

This is useful in cases where you replace a record file and want to generate a new cache for it. Generally, you don't want to remove cached data unless the record file has been
replaced with a new record file.

---

## TODOs

| Task                              | Priority |
|:----------------------------------|:--------:|
| Create Record as an object.       |  Medium  |
| Create Minimap as a builder.      |  Medium  |
| Create RecordParser as a builder. |  Medium  |

---

## Credits

* Thanks to [@happyleavesaoc](https://github.com/happyleavesaoc) for maintaining [aoc-mgz](https://github.com/happyleavesaoc/aoc-mgz) and for answering my questions on Discord.
* Thanks to [recanalyst](https://github.com/goto-bus-stop/recanalyst) for minimap colors.
