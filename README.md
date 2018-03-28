# music

Music library and embedding video for database course.  
Designed in Django.  

## Install

```
pip install -r requirements.txt
```

## Contributor

Haonan Wu  
Changxing Cao  


# Report
A.

![image alt text](image_0.png)

B.

**TABLE**

Users (uid, uname, uemail, ucity, ulogname, upw)

Primary Key: uid

Uid: Users’ id number, auto increase, not null;

Uname: Users’ name, can be null;

Uemail: Users’ email, can be null;

Ucity: The city users live in, can be null;

Ulogname: The nick name to log in, not null;

Upw: Password to log in, not null;

 

Track (tid, ttitle, tduration, tgenre, turl, aid)

Primary Key: tid

Foreign key: Track.aid references Artists.aid

Tid: songs’ id number, not null;

Ttitle: song’s name, not null;

Tduration: the total time that playing this song will cost, not null;

Tgenre: the genre of the song, not null;

Turl: the source web url of the song, not null;

Aid: the id number of Artist, not null;

 

Artists (aid, aname, adescript)

Primary Key: aid

Aid: the id number of Artist, not null;

Aname: artist’s name, not null;

Adescript: the description of the artist, not null;

 

Playlist (pid, ptitle, pdate, uid)

Primary Key: pid

Foreign key: Playlist.uid references Users.uid

Pid: the id number of playlist, not null;

Ptitle: the title name of playlist, not null;

Pdate: the datetime that the playlist created, not null;

Uid: users’ id number;

 

Album (alid, altitle, aldate)

Primary Key: alid

Alid: id number of album, not null;

Altitle: title name of the album, not null;

Aldate: the title date time that album released, not null;

 

AlbumTrack (alid, tid, aorder)

Primary Key: alid, tid

Foreign key: AlbumTrack.alid references Album.alid

                                	AlbumTrack.tid references Track.tid

Aorder: the order of one track in one album, not null;

 

PlaylistTrack (pid, tid, porder)

Primary Key: pid, tid

Foreign key: PlaylistTrack.pid references Playlist.pid

                     PlaylistTrack.tid references Track.tid

Porder: the order of one track in one playlist, not null;

 

Likes (uid, aid, ltimestamp)

Primary Key: uid, aid

Foreign key: Likes.uid references Users.uid

                     Likes.aid references Artists.tid

Ltimestamp: the timestamp when user likes one artist

 

Rate (uid, tid, rtimestamp, score)

Primary Key: uid, tid

Foreign key: Rate.uid references Users.uid

                     Rate.tid references Track.tid

Rtimestamp: the timestamp when user rates one track song

Score: the score that one user rates

Follow (flwerid, flweeid, ftimestamp)

Primary Key: flwerid, flweeid

Foreign key: Follow.flwerid references Users.uid

                     Follow.flweeid references Users.uid

Flwerid: the follower’s user id (A follows B, this will store A id)

Flweeid: the one who is followed id (store B id)

 

Play (uid, tid, ptype, sourceid, ptimestamp)

Primary Key: uid, tid, ptimestamp

Foreign key: Play.uid references Users.uid

                                            	Play.tid references Track.tid

Ptype: which kind of source the track playing come from, 0--album; 1--playlist; 2--others

Ptype=0,1,2.  Use "check ptype<=2 and ptype>=0"

Sourceid: the source id of the track, can be null;

Ptimestamp: the timestamp when user plays a song, not null

C.

INSERT INTO Users(uid, uname, uemail, ucity, ulogname, upw) values('1', 'NancyInQueens', 'niq@gmail.com', 'NY', 'nancyinqueens', '123456');

**Result:**

![image alt text](image_1.png)

SELECT art.aid, art.aname, COUNT(Track.tid)

FROM Artists as art, Track

WHERE art.aid = Track.aid

GROUP BY art.aid;

**Result:**

![image alt text](image_2.png)

SELECT art.aid

FROM Artists as art, Track

WHERE Track.aid = art.aid

AND Track.tgenre='Jazz'

GROUP BY Track.aid

HAVING 2*SUM(Track.tid) >= (

    SELECT SUM(t.tid)

    FROM Artists as a, Track as t

    WHERE a.aid = t.aid AND a.aid = Track.aid

    GROUP BY t.aid

    );

**Result:**

![image alt text](image_3.png)

INSERT INTO Rate(uid, tid, score, rtimestamp) values('1', '1', '5', now());

**Result:**

![image alt text](image_4.png)

SELECT pl.pid, pl.ptitle, pl.uid

FROM Playlist as pl, Users

WHERE pl.uid = Users.uid

AND Users.uid IN (

    SELECT Follow.flwerid

    FROM Follow, Users AS u

    WHERE u.uname = 'NancyInQueens'

    AND u.uid = Follow.flweeid

    );

**Result:**

![image alt text](image_5.png)

SELECT Track.tid, Track.ttitle

FROM Track, Artists AS art

WHERE Track.aid = art.aid

AND (CONTAIN(Track.ttitle, "love") OR CONTAIN(art.adescript, "love"));

**Result:**

![image alt text](image_6.png)

SELECT a1.aid, a2.aid

FROM Artists AS a1, Artists AS a2, Like AS l1, Like AS l2

WHERE a1.aid > a2.aid AND a1.aid = l1.aid AND a2.aid = l2.aid AND l1.uid = l2.uid

GROUP BY a1.aid, a2.aid

HAVING 2*SUM(l1.uid) >= (

    SELECT SUM(l3.uid)

    FROM Like AS l3

    WHERE a1.aid = l3.aid

    GROUP BY a1.aid

    )

AND 2*SUM(l1.uid) >= (

    SELECT SUM(l4.uid)

    FROM Like AS l4

    WHERE a2.aid = l4.aid

    GROUP BY a2.aid

    );

**Result:**

![image alt text](image_7.png)

D. 

**User Table**

![image alt text](image_8.png)

**Track Table**

![image alt text](image_9.png)

**Album Table**

![image alt text](image_10.png)

**Playlist Table**

![image alt text](image_11.png)

**Albumtrack Table**

![image alt text](image_12.png)

**Playlisttrack**

![image alt text](image_13.png)

**Artists Table**

![image alt text](image_14.png)

**Rate Table**

![image alt text](image_15.png)

**Likes Table**

![image alt text](image_16.png)

**Follow Table**

![image alt text](image_17.png)

## Design description:

In the table Play, we design a attribute (ptype) to show the source type of the track, if ptype equals to 0, it means that the song is played from a album, and the source id references to an album’s alid; if ptype equals to 1, it means that the song is played from playlist, and the source id references to a playlist’s pid; if ptype equals to 2, the song is played outside any playlist or album, so the source id is null. Because in different cases, the source id references to different attribute of different table, it can’t  be designed as a foreign key. And compared with using several tables to store the three kinds of sources, it will cost a little more space but easily be implemented.

In table Users, profile has ‘name’, ‘email’,’city’, they can be null and users can update their profile after they sign up and log in.

In table Track, we store url in this table, so when we need to play this song, we can just link the url with this song. 

In table Follow, there are two options that we can use, 1.use type to decide the two users’ relation; 2. Use the attribute to decide who follows who. We choose 2, and when we want to see which two users follow each other, we just need to add "a.uid<b.uid" to delete repeated data.				



## Show of the whole web: 

**User Table**

![image alt text](image_report/image_8.png)


**Track Table**

![image alt text](image_report/image_9.png)

**Album Table**

![image alt text](image_report/image_10.png)

**Playlist Table**

![image alt text](image_report/image_11.png)

**Albumtrack Table**

![image alt text](image_report/image_12.png)

**Playlisttrack**

![image alt text](image_report/image_13.png)

**Artists Table**

![image alt text](image_report/image_14.png)

**Rate Table**

![image alt text](image_report/image_15.png)

**Likes Table**

![image alt text](image_report/image_16.png)

**Follow Table**

![image alt text](image_report/image_17.png)






