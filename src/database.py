import sqlite3
import sys

from typing import List
from flashcard import Flashcard


class FlashcardDB:
    """Class for managing flashcard database."""
    def __init__(self) -> None:
        self.dbName = "flashcards.db"
        self.connection = sqlite3.connect(self.dbName)
        self.cursor = self.connection.cursor()
        self.connection.execute("PRAGMA foreign_keys = ON")     # Enable foreign keys

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
            cardFront TEXT NOT NULL,
            cardBack TEXT NOT NULL,
            groupId INTEGER,

            FOREIGN KEY (groupId) 
                REFERENCES FlashcardGroups(groupId) 
                ON DELETE CASCADE
        );
        """

        try:
            self.cursor.execute(createGroupTable)
            self.cursor.execute(createFlashcardsTable)
        except Exception as e:
            print("[ERROR] - creating database tables: ", e)
            sys.exit(1)

        self.connection.commit()


    def close(self):
        '''Closes the database. Should usually be called at the end of the program.''' 
        self.connection.close()


    def search(self, groupName: str) -> List[dict] | None:
        """
        Searches for groups that matches the provided group name.

        Args:
            groupName (str): Group to search for.

        Returns:
            List[{groupId, groupName}] or None.
        """

        sql = """
        SELECT groupId, groupName
        FROM FlashcardGroups
        WHERE groupName LIKE ?; 
        """
        searchPattern = f"%{groupName}%"
        self.cursor.execute(sql, (searchPattern,))
        result = self.cursor.fetchall()

        if result:
            return [{"groupId": row[0], "groupName": row[1]} for row in result]
        else:
            return None


    def insertCard(self, groupId: int, front: str, back: str) -> int:
        """
        Inserts a new card into the database.

        Returns:
            int: The ID of the newly created card.
        """

        sql = """INSERT INTO Flashcards (cardFront, cardBack, groupId) Values (?,?,?);"""
        self.cursor.execute(sql,(front, back, groupId))
        self.connection.commit()
        return self.cursor.lastrowid


    def insertGroup(self, groupName: str) -> int:
        """
        Inserts a new flashcard group into the database.

        Returns:
            int: The group ID of the newly created group.
        """

        sql = "INSERT INTO FlashcardGroups (groupName) VALUES (?);"
        self.cursor.execute(sql, (groupName,))
        self.connection.commit()
        return self.cursor.lastrowid


    def getCards(self, groupId: int) -> List[Flashcard] | None:
        """Returns all cards inside a group."""

        sql = """
        SELECT cardId, cardFront, cardBack
        FROM Flashcards
        WHERE groupId = ?;
        """
        self.cursor.execute(sql, (groupId,))
        result = self.cursor.fetchall()

        if result:
            return [Flashcard(row[0], row[1], row[2]) for row in result]
        else:
            return None


    def deleteCard(self, cardId: int):
        "Delete a specific card."
        sql = "DELETE FROM Flashcards WHERE cardId = ?;"
        self.cursor.execute(sql, (cardId,))
        self.connection.commit()


    def deleteGroup(self, groupId: int):
        "Delete group and all of its child."
        sql = "DELETE FROM FlashcardGroups WHERE groupId = ?;"
        self.cursor.execute(sql, (groupId,))
        self.connection.commit()


'''
1/2 childhood
1/4 college
1/3 batcher
2 2/3 gf
'''

