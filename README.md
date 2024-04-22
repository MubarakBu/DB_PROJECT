# DB_PROJECT

INFSCI 2710

## Project Title

SongRegistry (Song registration platform)

## Team Members

Hubert Asare

Jake Scrimager

Mubarak Buhaya

## Description

SongRegistry is a dedicated platform for songwriters and song owners to easily register and manage their songs, streamlining the process of song management and copyright tracking.

## Tables Description

• Users Table: Stores information about registered users (songwriters/song owners).

• Songs Table: Contains details of registered songs, including title, artist, genre, etc.

• Songwriters Table: Stores information about the songwriters associated with registered songs.

• Publishers Table: Stores information about publishers who may have rights to registered songs.

• Copyrights Table: Tracks copyright information for each registered song.

• Payments Table: Records payment transactions related to song registrations.

• Genres Table: Contains a list of genres for categorizing songs.

• Labels Table: Stores information about record labels associated with registered songs.

• Albums Table: Stores details of albums to which songs may belong.

• Metadata Table: Stores additional metadata for registered songs, such as release dates, durations, etc.

## Database Relationship Diagram

![Logo](https://github.com/MubarakBu/DB_PROJECT/blob/main/db_project.png?raw=true)

## Installation

1. Unzip attached zip file and open two new terminals.
2. Navigate to the project directories (App and SongRegistry inside DB_PROJECT folder)
   eg. on first terminal

```
cd SongRegistry
```

And on second terminal:

```
cd App
```

3. In each directory, create a Virtual Environment:

```
python -m venv env
```

4. Activate The Virtual Environments:

```
.\env\Scripts\activate
```

on Macbooks use:

```
source <venv_path>/bin/activate
```

5. Install Required Packages for each apps (each directory contains the requirement.txt file):

```
pip install -r requirement.txt
```

6. Create a Config File (Lecturer can skip this step we have attached this file):

• Create a new file named config.py in the SongRegistry directory.

• Copy the contents of the config file example and paste it into config.py.

• Replace the placeholder values with your actual configuration information.

7. Import The SQL Dump file to your MySQL

## Running application

1. After installation, run backend first (App.py in SongRegistry directory) with:

```
python3 app.py
```

before running frontend (App.py in App directory) with same command.

2. copy url and paste address in frontend terminal in browser. Frontend runs on localhost ipv6 and ipv4 for backend.
