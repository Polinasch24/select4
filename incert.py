import sqlalchemy

engine = sqlalchemy.create_engine(DSN = 'postgresql://postgres: PSchastlivaya@localhost:5432/postgres')
engine

connect = sqlalchemy.connect()
print(engine.table_names())

connection.execute('''INSERT INTO gerne
VALUES(1, 'Pop'),
(2, 'Rock'),
(3, 'Country'),
(4, 'Rap'),
(5, 'Texno'),
(6, 'Chanson');''')

connection.execute('''INSERT INTO artist
VALUES(1, 'Vintag', 'name'),
(2, 'Nikita', 'name'),
(3, 'Jandro', 'name'),
(4, 'Tisha', 'name'),
(5, 'Ruvi', 'name'),
(6, 'Galibri', 'name'),
(7, 'Basta', 'name'),
(8, 'Raim', 'name'),
(9, 'Splin', 'name'),
(10, 'The Weeknd', 'name'),
(11, 'Metric', 'name'),
(12, 'Zivert', 'name'),
(13, 'Leps', 'name'),
(14, 'CYGO', 'name'),
(15, 'RASA', 'name'),
(16, 'LOBODA', 'name'),
(17, 'TARAS', 'name'),
(18, 'Leningrad', 'name');''')

connection.execute('''INSERT INTO genreArt
VALUES(1, 9),
(1, 1),
(1, 10),
(2, 2),
(2, 11),
(2, 3),
(3, 12),
(3, 4),
(3, 13),
(4, 5),
(4, 14),
(4, 6),
(5, 15),
(5, 7),
(5, 16),,
(6, 8),
(6, 17
(6 ,18);''')

connection.execute('''INSERT INTO album
VALUES(1, 'union1', 2013),
(2, 'union2', 2014),
(3, 'union3', 2015),
(4, 'union4', 2016),
(5, 'union5', 2017),
(6, 'union6', 2018),
(7, 'union7', 2019),
(8, 'union8', 2020);''')

connection.execute('''INSERT INTO artAlbum
VALUES(1, 4),
(1, 8),
(2, 12)
(3, 7);''')

connection.execute('''INSERT INTO track
VALUES(1, 'track1', 95, 1),
(2, 'track2', 161, 1),
(3, 'track3', 217, 1),
(4, 'track1', 182, 2),
(5,	"track2", 240, 2),
(6,	"track3", 260, 3),
(7,	"track1", 210,	3),
(8	"track2", 187,	3),
(9	"track3", 200,	4),
(10, "track1", 280,	4),
(11, "track2", 180,	4),
(12, "track3", 170,	5),
(13, "track1", 235,	5),
(14, "track2", 150,	5),
(15, "track3", 160,	6),
(16, "track1", 90,	6),
(17, "track2", 120,	6),
(18, "track3", 125,	7),
(19, "track1", 180,	7),
(20, "track2", 220,	7);''')

connection.execute('''INSERT INTO collectionTrack
VALUES(1, 2),
(1,	3),
(2,	4),
(3,	5),
(4,	6),
(5,	2),
(5,	2),
(6,	2),
(7,	3),
(8,	4);''')

connection.execute('''INSERT INTO collection
VALUES(1, "Summer2013", "2013-06-01"),
(2,	"Summer2014",	"2014-06-01"),
(3,	"Winter2015",	"2015-12-01"),
(4,	"Winter2016",	"2016-12-01"),
(5,	"Summer2017",	"2017-06-01"),
(6,	"Summer2018",	"2018-06-01"),
(7,	"Winter2019",	"2019-12-01"),
(8,	"Winter2020",	"2020-12-01";''')
