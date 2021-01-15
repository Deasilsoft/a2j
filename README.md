# aoe2record-to-json

An Age of Empires II record analyzing API used to convert AoE2 records to JSON.

![LGTM Grade](https://img.shields.io/lgtm/grade/python/github/Deasilsoft/aoe2record-to-json?style=for-the-badge)
![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/Deasilsoft/aoe2record-to-json?style=for-the-badge)

## Setup

1. Pull the image from Docker Hub.

       docker pull deasilsoft/a2j:latest

2. Run container with the image and publish the port.

       docker run -p 8080:8080 deasilsoft/a2j

## Usage

This is an API ran as a Docker container. Mount to the `records` directory to add and remove records from the API.

### Endpoints

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
