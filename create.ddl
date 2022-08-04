CREATE TABLE kagawa_sightseeing(
    spot_id SERIAL PRIMARY KEY,
    spot_name TEXT,
    spot_latitude TEXT,
    spot_longitude TEXT,
    spot_opentime TEXT,
    spot_closetime TEXT,
    spot_nature INTEGER,
    spot_culture INTEGER,
    spot_view INTEGER
);

CREATE TABLE kagawa_udon(
    spot_id SERIAL PRIMARY KEY,
    spot_name TEXT,
    spot_latitude TEXT,
    spot_longitude TEXT,
    spot_rating FLOAT,
    spot_price FLOAT
);