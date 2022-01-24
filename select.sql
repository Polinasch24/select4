SELECT name, year FROM album
                          WHERE year = '2018';

SELECT name, duration FROM track
                          ORDER BY duration DESC;

SELECT name, duration FROM track
                          WHERE duration > '3.5';

SELECT name, year FROM collection
                          WHERE year BETWEEN '2018' AND '2020';

SELECT name FROM singer
                          WHERE name NOT LIKE '%% %%';

SELECT name FROM singer
                          WHERE name  LIKE '%%мой/my%%';