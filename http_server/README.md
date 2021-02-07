# HTTP server

Project with HTTP server for files access. It support several types of 
requests:

* GET
* POST
* OPTIONS

## How to start server

To start server you need to: 

1. Change path on top of `main.py` file
2. Go to `http_server` folder in command line
3. Use script.

```
usage: main.py [-h] [--port PORT] [--host HOST] [-df DATA_FOLDER]

Script for server setup

optional arguments:
  -h, --help            show this help message and exit
  --port PORT           Server port
  --host HOST           Server host
  -df DATA_FOLDER, --data-folder DATA_FOLDER
                        Folder with all data

```