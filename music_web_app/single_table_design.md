Single Table Design Recipe Template

1. Extract nouns from the user stories or specification

As a music lover,
So I can organise my records,
I want to keep a list of albums' titles.

As a music lover,
So I can organise my records,
I want to keep a list of albums' release years.
Nouns:

album, title, release year, artist_id

2. Infer the Table Name and Columns

Record	Properties
album	title, release year, artist_id
Name of the table (always plural): albums

Column names: title, release_year, artist_id

3. Decide the column types

id: SERIAL
title: text
release_year: int
artist_id: int

4. Write the SQL

CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int,
  artist_id int
);

5. Create the table

psql -h 127.0.0.1 music_web_app < music_web_app.sql