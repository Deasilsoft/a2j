# deasilsoft/a2j

A Restful JSON API for analyzing Age of Empires II records.

[![Code Tests](https://img.shields.io/github/workflow/status/deasilsoft/a2j/Run%20a2j%20Tests?label=pytest&logo=pytest&logoWidth=18)](https://github.com/Deasilsoft/a2j/actions/workflows/tests.yaml)
[![Codecov Coverage](https://img.shields.io/codecov/c/github/deasilsoft/a2j?logo=codecov&logoWidth=18)](https://app.codecov.io/gh/Deasilsoft/a2j)
[![Code Inspector Score](https://www.code-inspector.com/project/25065/score/svg)](https://frontend.code-inspector.com/project/25065/dashboard)
[![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/deasilsoft/a2j/main?label=CodeFactor&logo=codefactor&logoWidth=18)](https://www.codefactor.io/repository/github/deasilsoft/a2j)
[![LGTM Alerts](https://img.shields.io/lgtm/alerts/github/Deasilsoft/a2j?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Deasilsoft/a2j/context:python)  
[![Docker Build](https://img.shields.io/github/workflow/status/deasilsoft/a2j/Build%20and%20Push%20a2j%20to%20Docker%20Hub?logo=docker&logoWidth=18)](https://github.com/Deasilsoft/a2j/actions/workflows/docker-hub.yaml)
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

### Direct Download & Docker Compose (Development)

1. Clone deasilsoft/a2j from Github and open the project root directory:

       git clone https://github.com/Deasilsoft/a2j.git
       cd a2j

2. Make changes to **docker-compose.yml** as you desire.

3. Run the Docker container(s) with:

       docker compose up --build -d

### Using Only Docker (Production)

1. Pull the image from Docker Hub.

       docker pull deasilsoft/a2j:latest

2. Run the Docker container.

       docker run -d --name a2j -v ABSOLUTE_PATH_TO_RECORDS:/home/a2j/records --restart always deasilsoft/a2j:latest

*Remember to replace **ABSOLUTE_PATH_TO_RECORDS** with your own value.*

Read more about the [`docker run`](https://docs.docker.com/engine/reference/commandline/run/) syntax.

---

## Usage

This is a Restful API running in a Docker container **behind your secure firewall**. You can add more record files from the host by placing them inside the directory
named `records` in your project root. The purpose of the API is to easily and efficiently retrieve the data you want from an Age of Empires II record file. The output data is JSON,
which is easy to handle in any programming language.

### Endpoints

    container_name:5000/
    container_name:5000/minimap/<record>/?[scale=1-15|5]
    container_name:5000/record/<record>/<commands...>/

Whenever you get a list of `endpoints` from a request, you can add one of them at the end of your current path.

---

## Examples

### GET

#### Record Data

This example will retrieve a JSON object of all the `teams` and `players` from the `test.mgz` record.

    curl container_name:5000/record/test.mgz/teams/players/

#### Minimap

This example will retrieve a PNG image with our interpretation of the Age of Empires II minimap.

    curl container_name:5000/minimap/test.mgz/

### DELETE

#### Cached Data

To delete all **cached data** from a `record` you can do the following.

    curl -X DELETE container_name:5000/record/test.mgz/

This is useful in cases where you replace a `record` and want to generate a new cache, or for a general cleanup. Generally, you don't want to remove cached data unless the `record`
has changed.

---

## Credits

* Thanks to [@happyleavesaoc](https://github.com/happyleavesaoc) for maintaining [aoc-mgz](https://github.com/happyleavesaoc/aoc-mgz) and for answering my questions on Discord.
* Thanks to [recanalyst](https://github.com/goto-bus-stop/recanalyst) for minimap colors.
