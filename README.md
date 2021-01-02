# aoe2-record-to-json

A tool used to convert AoE2 records to JSON.

## Setup

1. Clone repository.

       git clone https://github.com/Deasilsoft/aoe2-record-handler.git

2. Install mgz in project root.

       pip install mgz

## Usage

    append.py <file> <content>
    parse.py <file> <command...>
    remove.py <file>

## Example

    append.py example.aoe2record <binary values>
    append.py example.aoe2record <binary values>
    append.py example.aoe2record <binary values>

    parse.py example.aoe2record players teams
