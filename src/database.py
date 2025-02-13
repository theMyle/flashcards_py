import sqlite3

dbName = "flashcards.db"

connection = sqlite3.connect(dbName)
cursor = connection.cursor()

# Enable foreign keys
connection.execute("PRAGMA foreign_keys = ON")

# Create Tables
createGroupTable = """
CREATE TABLE IF NOT EXISTS FlashcardGroups (
    groupId INTEGER PRIMARY KEY AUTOINCREMENT,
    groupName TEXT NOT NULL
);
"""

createFlashcardsTable = """
CREATE TABLE IF NOT EXISTS Flashcards (
    cardId INTEGER PRIMARY KEY AUTOINCREMENT,
    cardFont TEXT NOT NULL,
    cardBack TEXT NOT NULL,
    groupId INTEGER,
    FOREIGN KEY (groupId) 
        REFERENCES FlashcardGroups(groupId) 
        ON DELETE CASCADE
);
"""

try:
    cursor.execute(createGroupTable)
    cursor.execute(createFlashcardsTable)
except Exception as e:
    print("[ERROR] - creating database tables: ", e)


# Execute sqlite commands
# cursor.execute()

# Save changes
connection.commit()

# Close the connection
connection.close()
