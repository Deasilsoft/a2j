# aoe2record-to-json

An Age of Empires II record analyzing tool used to convert AoE2 records to JSON.

![LGTM Grade](https://img.shields.io/lgtm/grade/python/github/Deasilsoft/aoe2record-to-json?style=for-the-badge)
![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/Deasilsoft/aoe2record-to-json?style=for-the-badge)

## Setup

1. Pull the image from Docker Hub.

       docker pull deasilsoft/a2j:latest

2. Run container with the image and publish the port.

       docker run -p 8080:8080 deasilsoft/a2j

## Usage

    curl localhost:8080/a2j/
    curl localhost:8080/a2j/v1/
    curl localhost:8080/a2j/v1/parse/

## Example

    curl localhost:8080/a2j/v1/parse/teams/players/?record=test.mgz
