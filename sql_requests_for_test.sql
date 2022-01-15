SELECT CASE
    WHEN home_team < away_team
    THEN concat(home_team, ' - ', away_team)
    ELSE concat(away_team, ' - ', home_team)
    END AS game,
    count(play_id) AS games_count
FROM
  event_entity
GROUP BY game;

SELECT b.client_number, count(if(ev.outcome='win',1,null)) AS Побед, count(if(ev.outcome='lose',1,null)) AS Поражений
FROM bid b
    JOIN event_value ev
        ON b.play_id = ev.play_id
GROUP BY b.client_number;