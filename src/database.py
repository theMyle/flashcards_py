import sqlite3
import sys
from datetime import datetime, timedelta

from typing import List, Optional
from flashcard import Flashcard, FlashcardGroup


class FlashcardDB:
    """Class for managing flashcard database"""
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
            lastReview TEXT,
            nextReview TEXT,
            interval INTEGER DEFAULT 1,

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

        today = (datetime.now().date() - timedelta(days=1)).isoformat() # Set lastReview to yesterday
        sql = """INSERT INTO Flashcards (cardFront, cardBack, groupId, lastReview, nextReview, interval) Values (?,?,?,?,?,?);"""
        self.cursor.execute(sql,(front, back, groupId, today, today, 1))
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

    def getGroups(self) -> List[FlashcardGroup] | None:
        """
        Returns flashcard groups from the database.
        """

        sql = """
        SELECT * 
        FROM FlashcardGroups;
        """

        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return [FlashcardGroup(group_id=row[0], group_name=row[1]) for row in result]

    def getGroupInfo(self, groupId: int) -> Optional[FlashcardGroup]:
        """
        Returns group info of a specific flashcard group.
        """

        sql = """
        SELECT * 
        FROM FlashcardGroups
        WHERE groupId = ?;
        """

        self.cursor.execute(sql, (groupId,))
        result = self.cursor.fetchone()

        if result:
            return FlashcardGroup(group_id=result[0], 
                                  group_name=result[1])

        return None

    def updateGroupInfo(self, groupId: int, newGroupName: str):
        """
        Updates the name of a specific flashcard group.

        Args:
            groupId (int): The ID of the group to update.
            newGroupName (str): The new name for the group.
        """

        sql = """
        UPDATE FlashcardGroups
        SET groupName = ?
        WHERE groupId = ?;
        """

        self.cursor.execute(sql, (newGroupName, groupId))
        self.connection.commit()

    def getCards(self, groupId: int) -> List[Flashcard] | None:
        """Returns all cards inside a group."""

        sql = """
        SELECT cardId, cardFront, cardBack, lastReview, nextReview, interval
        FROM Flashcards
        WHERE groupId = ?;
        """
        self.cursor.execute(sql, (groupId,))
        result = self.cursor.fetchall()

        if result:
            return [Flashcard(row[0], 
                              row[1], 
                              row[2], 
                              datetime.fromisoformat(row[3]), 
                              datetime.fromisoformat(row[4]), 
                              row[5]) for row in result]
        else:
            return None

    def deleteCard(self, cardId: int):
        "Deletes a specific card."
        sql = "DELETE FROM Flashcards WHERE cardId = ?;"
        self.cursor.execute(sql, (cardId,))
        self.connection.commit()


    def deleteGroup(self, groupId: int):
        """Delete group and all of its children"""
        sql = "DELETE FROM FlashcardGroups WHERE groupId = ?;"
        self.cursor.execute(sql, (groupId,))
        self.connection.commit()


    def updateCard(self, cardId: int, newFront: str, newBack: str):
        """Update a specific card based on cardId"""
        sql = "UPDATE Flashcards SET cardFront=?, cardBack=? WHERE cardId = ?"
        self.cursor.execute(sql, (newFront, newBack, cardId))
        self.connection.commit()


    def updateCardReview(self, cardId: int, lastReview: datetime, nextReview: datetime, interval: int):
        """FOR REVIEW EDITS: Update a specific card based on cardId"""
        sql = "UPDATE Flashcards SET lastReview=?, nextReview=?, interval=? WHERE cardId = ?"
        self.cursor.execute(sql, (lastReview.isoformat(), nextReview.isoformat(), interval, cardId))
        self.connection.commit()

    def getClosestReviewDate(self):
        sql = """
            SELECT nextReview 
            FROM Flashcards
            WHERE nextReview IS NOT NULL
            ORDER BY date(nextReview) ASC
            LIMIT 1;
            """
        self.cursor.execute(sql)
        result = self.cursor.fetchone()

        if result:
            return datetime.fromisoformat(result[0])
        else:
            return None

db:FlashcardDB = FlashcardDB()
