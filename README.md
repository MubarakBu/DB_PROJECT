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

•	Users Table: Stores information about registered users (songwriters/song owners).

•	Songs Table: Contains details of registered songs, including title, artist, genre, etc.

•	Songwriters Table: Stores information about the songwriters associated with registered songs.

•	Publishers Table: Stores information about publishers who may have rights to registered songs.

•	Copyrights Table: Tracks copyright information for each registered song.

•	Payments Table: Records payment transactions related to song registrations.

•	Genres Table: Contains a list of genres for categorizing songs.

•	Labels Table: Stores information about record labels associated with registered songs.

•	Albums Table: Stores details of albums to which songs may belong.

•	Metadata Table: Stores additional metadata for registered songs, such as release dates, durations, etc.




## Database Relationship Diagram

![Logo](https://github.com/MubarakBu/DB_PROJECT/blob/main/db_project.png?raw=true)

## Installation 

1. Clone the repository
2. Navigate to the project directory

```
cd SongRegistry
```
3. Create a Virtual Environment:
```
python -m venv env
```
4. Activate The Virtual Environment:
```
.\env\Scripts\activate
```
5. Install Required Packages:
```
pip install -r requirements.txt
```
6. Create a Config File:

• Create a new file named config.py in the SongRegistry directory.

• Copy the contents of the config file example and paste it into config.py.

• Replace the placeholder values with your actual configuration information.
