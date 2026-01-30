import sqlite3
import streamlit as st

DB_NAME = "moviess.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_movie_table():
    with get_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS MOVIES (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                TITLE TEXT NOT NULL,
                DIRECTOR TEXT NOT NULL,
                YEAR INT NOT NULL,
                RATING REAL NOT NULL,
                WATCHED BOOL NOT NULL
            )
        ''')

def add_movie(title, director, year, rating):
    with get_connection() as conn:
        conn.execute("INSERT INTO MOVIES (TITLE, DIRECTOR, YEAR, RATING, WATCHED) VALUES (?, ?, ?, ?, ?)",
                     (title, director, year, rating, 0))

def get_all_movies():
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM MOVIES")
        return cur.fetchall()

def mark_movie_watched(movie_id):
    with get_connection() as conn:
        conn.execute("UPDATE MOVIES SET WATCHED = 1 WHERE ID = ?", (movie_id,))

def search_movies(column, value):
    query = f"SELECT * FROM MOVIES WHERE {column} LIKE ?"
    param = f"%{value}%" if column in ["TITLE", "DIRECTOR"] else value
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(query, (param,))
        return cur.fetchall()

def update_movie(movie_id, column, value):
    with get_connection() as conn:
        conn.execute(f"UPDATE MOVIES SET {column} = ? WHERE ID = ?", (value, movie_id))

def delete_movie(movie_id):
    with get_connection() as conn:
        conn.execute("DELETE FROM MOVIES WHERE ID = ?", (movie_id,))

def clear_movies():
    with get_connection() as conn:
        conn.execute("DELETE FROM MOVIES")

def display_movies(movies):
    if not movies:
        st.info("No movies found.")
        return
    for row in movies:
        st.write(f"**ID**: {row[0]}, **Title**: {row[1]}, **Director**: {row[2]}, "
                 f"**Year**: {row[3]}, **Rating**: {row[4]}, **Watched**: {'Yes' if row[5] else 'No'}")

# ----------------- Streamlit UI ----------------- #

st.set_page_config(page_title="🎬 Movie Manager", layout="centered")
st.title("🎬 Movie Manager with SQLite")

create_movie_table()

tabs = st.tabs(["Add Movie", "View Movies", "Mark as Watched", "Search", "Update Movie", "Delete", "Clear All"])

# Add Movie
with tabs[0]:
    st.header("Add a New Movie")
    title = st.text_input("Title")
    director = st.text_input("Director")
    year = st.number_input("Year", step=1, format="%d")
    rating = st.number_input("Rating (0.0 - 10.0)", step=0.1, format="%.1f")

    if st.button("Add Movie"):
        if title and director:
            add_movie(title.strip(), director.strip(), int(year), float(rating))
            st.success(f"Movie '{title}' added.")
        else:
            st.warning("Please provide both title and director.")

# View Movies
with tabs[1]:
    st.header("All Movies")
    movies = get_all_movies()
    display_movies(movies)

# Mark as Watched
with tabs[2]:
    st.header("Mark a Movie as Watched")
    movies = get_all_movies()
    ids = [str(row[0]) + " - " + row[1] for row in movies if not row[5]]
    selected = st.selectbox("Select movie", ids)
    if st.button("Mark as Watched"):
        if selected:
            movie_id = int(selected.split(" - ")[0])
            mark_movie_watched(movie_id)
            st.success("Movie marked as watched.")

# Search Movies
with tabs[3]:
    st.header("Search Movies")
    search_by = st.selectbox("Search by", ["Title", "Director", "Year", "Rating"])
    keyword = st.text_input("Enter search value")
    if st.button("Search"):
        col_map = {"Title": "TITLE", "Director": "DIRECTOR", "Year": "YEAR", "Rating": "RATING"}
        result = search_movies(col_map[search_by], keyword)
        display_movies(result)

# Update Movie
with tabs[4]:
    st.header("Update Movie Info")
    movies = get_all_movies()
    ids = [f"{row[0]} - {row[1]}" for row in movies]
    selected = st.selectbox("Select movie to update", ids)
    field = st.selectbox("Field to update", ["Title", "Director", "Year", "Rating"])
    new_val = st.text_input("New value")

    if st.button("Update"):
        if selected and new_val:
            movie_id = int(selected.split(" - ")[0])
            field_map = {"Title": "TITLE", "Director": "DIRECTOR", "Year": "YEAR", "Rating": "RATING"}
            col = field_map[field]
            try:
                if col == "YEAR":
                    new_val = int(new_val)
                elif col == "RATING":
                    new_val = float(new_val)
                update_movie(movie_id, col, new_val)
                st.success("Movie updated.")
            except ValueError:
                st.error(f"Invalid value for {field}")

# Delete Movie
with tabs[5]:
    st.header("Delete a Movie")
    movies = get_all_movies()
    ids = [f"{row[0]} - {row[1]}" for row in movies]
    selected = st.selectbox("Select movie to delete", ids)
    if st.button("Delete"):
        if selected:
            movie_id = int(selected.split(" - ")[0])
            delete_movie(movie_id)
            st.success("Movie deleted.")

# Clear All
with tabs[6]:
    st.header("Clear All Movies")
    confirm = st.checkbox("Yes, I want to delete all movies permanently.")
    if st.button("Clear All") and confirm:
        clear_movies()
        st.success("All movies deleted.")

