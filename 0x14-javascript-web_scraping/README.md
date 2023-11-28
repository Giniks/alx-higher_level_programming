# Project Title: JavaScript Web Scraping Project

# Project Overview

This project includes scripts written in JavaScript for web scraping tasks. The scripts are designed to be compliant with semistandard and follow the rules of Standard + semicolons, with a reference to the AirBnB style.

## Table of Contents

- [Description](#description)
- [Tasks](#tasks)
  - [Readme](#readme)
  - [Write Me](#write-me)
  - [Status Code](#status-code)
  - [Star Wars Title](#star-wars-title)
  - [Star Wars Wedge Antilles](#star-wars-wedge-antilles)
  - [Request Store](#request-store)
  - [How Many Completed?](#how-many-completed)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)
- [Acknowledgements](#acknowledgements)

## Description

The project consists of JavaScript scripts for various web scraping tasks, including reading and writing files, fetching status codes, interacting with the Star Wars API, and more.

## Tasks

### Readme

Write a script that reads and prints the content of a file.

```bash
$ ./0-readme.js cisfun
C is super fun!
```

### Write Me

Write a script that writes a string to a file.

```bash
$ ./1-writeme.js my_file.txt "Python is cool"
$ cat my_file.txt ; echo ""
Python is cool
```

### Status Code

Write a script that displays the status code of a GET request.

```bash
$ ./2-statuscode.js https://alx-intranet.hbtn.io/status
code: 200
```

### Star Wars Title

Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

```bash
$ ./3-starwars_title.js 1
A New Hope
```

### Star Wars Wedge Antilles

Write a script that prints the number of movies where the character “Wedge Antilles” is present.

```bash
$ ./4-starwars_count.js https://swapi-api.alx-tools.com/api/films/
3
```

### Request Store

Write a script that gets the contents of a webpage and stores it in a file.

```bash
$ ./5-request_store.js http://loripsum.net/api loripsum
$ cat loripsum
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Haec quo modo conveniant, non sane intellego. ...
```

### How Many Completed?

Compute the number of tasks completed by user id.

```bash
$ ./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
{ '1': 11, '2': 8, '3': 7, '4': 6, '5': 12, '6': 6, '7': 9, '8': 11, '9': 8, '10': 12 }
```

## Installation

Follow these steps to install Node 14 and the required modules:

```bash
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
$ sudo npm install semistandard --global
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

## Usage

Ensure your files are executable, and run the scripts as demonstrated in the task descriptions.

## Dependencies

- Node.js 14
- semistandard
- request

## Contributing

Feel free to contribute by following the guidelines in the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## License

This project is licensed under the [MIT License](LICENSE).

## Author

- [Ginika Elizabeth Nna](https://github.com/Giniks)

## Acknowledgements

Special thanks to the contributors and organizations that made this project possible.
```

Customize this template further based on your specific project details.
