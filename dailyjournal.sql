CREATE TABLE `Entries` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `concept` TEXT NOT NULL,
    `entry` TEXT NOT NULL,
    `date` Date,
    `mood_id` INTEGER NOT NULL
);
CREATE TABLE `Moods` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `label` TEXT NOT NULL
);
INSERT INTO `Entries`
VALUES (
        null,
        "Learned alot",
        "its easy as 123",
        1598458543321,
        3
    );
INSERT INTO `Entries`
VALUES (null, "123", "its easy as ABC", 1598458548239, 3);
INSERT INTO `Entries`
VALUES (
        null,
        "CODE",
        "IS Makingme sad",
        1598458559152,
        2
    );
INSERT INTO `Moods`
VALUES (null, "Happy");
INSERT INTO `Moods`
VALUES (null, "Sad");
INSERT INTO `Moods`
VALUES (null, "Angry");
INSERT INTO `Moods`
VALUES (null, "Ok");