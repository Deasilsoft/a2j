# aoe2record-to-json

An Age of Empires II record analyzing tool used to convert AoE2 records to JSON.

## Requirements

Python 3.6 or later (check Actions)

## Setup

1. Clone repository.

       git clone https://github.com/Deasilsoft/aoe2record-to-json.git

2. Install mgz in project root.

       pip install mgz

## Usage

All functions are executed from `app.py`.

Available functions:

     help
     parse <record> <command> [...]

Available commands:

     completed, dataset, encoding, file_hash, hash, language, mirror, owner, platform
     restored, version, chat, diplomacy, players, profiles, ratings, teams, achievements
     duration, map, objects, postgame, settings, start_time

## Example

    app.py parse example.aoe2record players teams objects
