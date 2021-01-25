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
VALUES (null, "ABCC", "its easy as 123", 12 / 12 / 12, 3);
INSERT INTO `Entries`
VALUES (null, "123", "its easy as ABC", 12 / 12 / 12, 3);
INSERT INTO `Entries`
VALUES (null, "CODE", "IS REALLY HARD", 12 / 12 / 12, 3);