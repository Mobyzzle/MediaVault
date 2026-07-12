CREATE TABLE images_v3(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT DEFAULT 'Untitled',
    file_path TEXT,
    source_url TEXT,
    file_size INTEGER,
    width INTEGER,
    height INTEGER,
    date_added TEXT NOT NULL DEFAULT (CURRENT_TIMESTAMP),
    last_viewed TEXT,
    viewcount INTEGER NOT NULL DEFAULT 0,
    rating INTEGER NOT NULL DEFAULT 1 CHECK (rating BETWEEN 1 AND 10),
    favourite INTEGER NOT NULL DEFAULT 0 CHECK (favourite IN (0,1)),
    CHECK( file_path IS NOT NULL OR source_url IS NOT NULL)
);