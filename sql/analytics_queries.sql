CREATE DATABASE streamsight;
USE streamsight;
SHOW DATABASES;

USE streamsight;

CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(20),
    country VARCHAR(50),
    subscription_plan VARCHAR(30)
);

CREATE TABLE shows (
    show_id INT PRIMARY KEY,
    title VARCHAR(150),
    genre VARCHAR(50),
    release_year INT,
    duration_minutes INT,
    content_type VARCHAR(20)
);

CREATE TABLE watch_history (
    watch_id INT PRIMARY KEY,
    user_id INT,
    show_id INT,
    watch_date DATE,
    watch_time_minutes INT,
    rating DECIMAL(2,1),

    FOREIGN KEY (user_id)
        REFERENCES users(user_id),

    FOREIGN KEY (show_id)
        REFERENCES shows(show_id)
);

SHOW TABLES;

USE streamsight;

DESCRIBE users;



USE streamsight;

DROP TABLE IF EXISTS watch_history;
DROP TABLE IF EXISTS shows;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    user_id VARCHAR(10) PRIMARY KEY,
    age_group VARCHAR(20),
    city VARCHAR(50),
    subscription_plan VARCHAR(30)
);

CREATE TABLE shows (
    show_id VARCHAR(10) PRIMARY KEY,
    title VARCHAR(150),
    genre VARCHAR(50),
    content_type VARCHAR(20)
);

CREATE TABLE watch_history (
    watch_id VARCHAR(10) PRIMARY KEY,
    user_id VARCHAR(10),
    show_id VARCHAR(10),
    watch_minutes INT,
    watch_date DATE,

    FOREIGN KEY (user_id)
        REFERENCES users(user_id),

    FOREIGN KEY (show_id)
        REFERENCES shows(show_id)
);

DESCRIBE users;
DESCRIBE shows;
DESCRIBE watch_history;

USE streamsight;

SELECT COUNT(*) AS total_users

use streamsight;
select count(*) as total_watch_records
from watch_history;

SELECT *
FROM watch_history
LIMIT 10;

USE streamsight;
SELECT
    (SELECT COUNT(*) FROM users) AS total_users,
    (SELECT COUNT(*) FROM shows) AS total_shows,
    (SELECT COUNT(*) FROM watch_history)
        AS total_watch_records,
    (SELECT SUM(watch_minutes) FROM watch_history)
        AS total_watch_minutes,
    ROUND(
        (SELECT SUM(watch_minutes) FROM watch_history) / 60,
        2
    ) AS total_watch_hours;
    
    USE streamsight;

SELECT
    s.genre,
    COUNT(wh.watch_id) AS total_watch_records,
    SUM(wh.watch_minutes) AS total_watch_minutes,
    ROUND(SUM(wh.watch_minutes) / 60, 2)
        AS total_watch_hours
FROM watch_history wh
JOIN shows s
    ON wh.show_id = s.show_id
GROUP BY s.genre
ORDER BY total_watch_minutes DESC
LIMIT 5;

USE streamsight;
SELECT
    u.subscription_plan,
    COUNT(DISTINCT u.user_id)
        AS active_users,
    COUNT(wh.watch_id)
        AS total_watch_records,
    SUM(wh.watch_minutes)
        AS total_watch_minutes,
    ROUND(SUM(wh.watch_minutes) / 60, 2)
        AS total_watch_hours
FROM users u
JOIN watch_history wh
    ON u.user_id = wh.user_id
GROUP BY u.subscription_plan
ORDER BY total_watch_minutes DESC;

USE streamsight;
SELECT
    s.show_id,
    s.title,
    s.genre,
    s.content_type,
    COUNT(wh.watch_id) AS total_watch_records,
    SUM(wh.watch_minutes) AS total_watch_minutes,
    ROUND(SUM(wh.watch_minutes) / 60, 2)
        AS total_watch_hours
FROM shows s
JOIN watch_history wh
    ON s.show_id = wh.show_id
GROUP BY
    s.show_id,
    s.title,
    s.genre,
    s.content_type
ORDER BY total_watch_minutes DESC
LIMIT 10;

USE streamsight;
SELECT
    MONTH(watch_date) AS watch_month,
    COUNT(*) AS total_records,
    SUM(watch_minutes) AS total_watch_minutes
FROM watch_history
GROUP BY MONTH(watch_date)
ORDER BY watch_month;

USE streamsight;
SELECT
    u.user_id,
    u.city,
    u.subscription_plan,
    COUNT(wh.watch_id) AS total_watch_records,
    SUM(wh.watch_minutes) AS total_watch_minutes,
    ROUND(AVG(wh.watch_minutes), 2)
        AS average_watch_minutes
FROM users u
JOIN watch_history wh
    ON u.user_id = wh.user_id
GROUP BY
    u.user_id,
    u.city,
    u.subscription_plan
ORDER BY average_watch_minutes DESC
LIMIT 10;

USE streamsight;
SELECT
    s.title,
    s.genre,
    SUM(wh.watch_minutes) AS total_watch_minutes,
    ROW_NUMBER() OVER (
        ORDER BY SUM(wh.watch_minutes) DESC
    ) AS show_rank
FROM shows s
JOIN watch_history wh
    ON s.show_id = wh.show_id
GROUP BY
    s.show_id,
    s.title,
    s.genre
ORDER BY show_rank;

USE streamsight;
SELECT
    s.content_type,
    COUNT(wh.watch_id) AS total_watch_records,
    SUM(wh.watch_minutes) AS total_watch_minutes,
    ROUND(SUM(wh.watch_minutes) / 60, 2)
        AS total_watch_hours
FROM shows s
JOIN watch_history wh
    ON s.show_id = wh.show_id
GROUP BY s.content_type
ORDER BY total_watch_minutes DESC;

USE streamsight;
SELECT
    u.city,
    COUNT(wh.watch_id) AS total_watch_records,
    SUM(wh.watch_minutes) AS total_watch_minutes,
    ROUND(SUM(wh.watch_minutes) / 60, 2)
        AS total_watch_hours
FROM users u
JOIN watch_history wh
    ON u.user_id = wh.user_id
GROUP BY u.city
ORDER BY total_watch_minutes DESC;

USE streamsight;
SELECT
    COUNT(*) AS total_records,
    SUM(user_id IS NULL) AS missing_user_ids,
    SUM(show_id IS NULL) AS missing_show_ids,
    SUM(watch_minutes IS NULL) AS missing_watch_minutes,
    SUM(watch_date IS NULL) AS missing_watch_dates
FROM watch_history;
