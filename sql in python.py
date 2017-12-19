import sqlite3
connection = sqlite3.connect("company.db")
sqlite3.connect("company.db")


/** Crypto coin ballances **/

CREATE TABLE coins ('crypto-coin' INTEGER PRIMARY KEY, name TEXT, quantity NUMERIC );

INSERT INTO coins VALUES (1, "Bitcoin", 0.0359215267539770623);
INSERT INTO coins VALUES (2, "Etherium", 0.016973837135966008);
INSERT INTO coins VALUES (3, "TrezarCoin", 64.793118);
SELECT * FROM coins;



insert into wallets valueS ('0x1c0706C01f2b70e6247605B314298930F89Db26a','pirl',45.6434);
insert into wallets valueS ('0xc5416c82aadf5fa5fc9f2a4454aeb00a93ed8e2c','eth',0.0160343618804);
insert into wallets valueS ('t1U4PrAWnnryBQxnNaYxxua9VLYSkDsMV8h','zcash',0.0124286540001);



insert into computers valueS (420,'daniels pc','28.6 h/s', 215);
insert into computers valueS (153,'garage','25.3 h/s', 112);
insert into computers valueS (540,'a','30.6 h/s', 533);

select * from computers;
select * from wallets;



