CREATE TABLE images_v4(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL DEFAULT "Untitled",
file_path TEXT,
source_url TEXT,
thumbnail_path TEXT,
file_hash TEXT UNIQUE NOT NULL,
file_size INTEGER,
height INTEGER,
width INTEGER,
aspect_ratio TEXT,
date_added TEXT NOT NULL DEFAULT (CURRENT_TIMESTAMP),
last_viewed TEXT,
viewcount INTEGER NOT NULL DEFAULT 0,
rating INTEGER NOT NULL DEFAULT 0 CHECK (rating between 0 AND 5),
favourite INTEGER NOT NULL DEFAULT 0 CHECK (favourite in (1,0)),

CHECK(file_path IS NOT NULL OR source_url IS NOT NULL)


	
);
