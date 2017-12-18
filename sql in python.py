import sqlite3
connection = sqlite3.connect("company.db")
sqlite3.connect("company.db")


/** Crypto coin ballances **/

CREATE TABLE coins ('crypto-coin' INTEGER PRIMARY KEY, name TEXT, quantity NUMERIC );

INSERT INTO coins VALUES (1, "Bitcoin", 0.0359215267539770623);
INSERT INTO coins VALUES (2, "Etherium", 0.016973837135966008);
INSERT INTO coins VALUES (3, "TrezarCoin", 64.793118);
SELECT * FROM coins;
