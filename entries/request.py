import sqlite3
import json
from model import Entry
from model import Mood


def get_all_entries():
    # Open a connection to the database
    with sqlite3.connect("./dailyjournal.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.mood_id,
            m.label,
            m.id
        FROM Entries e
        JOIN Moods m on m.id = e.mood_id
        """)

        # Initialize an empty list to hold all animal representations
        entries = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            entry = Entry(row['id'], row['concept'], row['entry'],
                          row['date'], row['mood_id'])

            mood = Mood(row['id'], row['label'])

            entry.mood = mood.__dict__

            entries.append(entry.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(entries)


def get_single_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.mood_id
        FROM Entries e
        WHERE e.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        entry = Entry(data['id'], data['concept'],
                      data['entry'], data['date'], data['mood_id'])

        return json.dumps(entry.__dict__)


def delete_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Entries
        WHERE id = ?
        """, (id, ))


def get_entries_by_search_term(search_term):
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.entry,
            e.concept,
            e.date,
            e.moodId,
            m.mood
        FROM Entries e
        Join Moods m on m.id = e.moodId
        WHERE e.entry Like ?
        """, ("%" + search_term + "%"), )

        entries = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            entry = Entry(row['id'], row['concept'],
                          row['date'], row['moodId'], row['moodId'])
            mood = Mood(row['moodId'], row['mood'])
            entry.mood = mood.__dict__
            entries.append(entry.__dict__)

    return json.dumps(entries)
