# CHIP Maker

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

Generate a CHIP-0007 format for CSV Files in an organized output

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

You will need to have Python 3.6 or higher installed on your machine.

```
Install Python 3.7 or higher
```

Install [Python](https://www.python.org/downloads/)


### Installing

Clone project

```
git clone 
```


## Usage <a name = "usage"></a>

This is how to use the script:

1. Place CSV files to generate in the same folder as the main.py file,
2. Run the script with the following command:

```python
python main.py -f <filename.csv> -t <team_name>
```

```txt
-f : Takes the file name to generate chips for
-t : Takes the team name to generate chips for
```

This will generate a nice output, making your new dir structure look like this

```txt
├───<team_name>
│   ├───chips
│   │   ├───a.json
│   │   |───b.json
│   |───<filename.output.csv>
|--main.py
```
