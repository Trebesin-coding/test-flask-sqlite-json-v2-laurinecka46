import sqlite3

connection = sqlite3.connect("filmy.db")
# Proč je connection podtržené? Oprav chybu
cursor = connection.cursor()


# Oprav vytváření tabulky - hodnocení je číselné
cursor.execute(
    """CREATE TABLE IF NOT EXISTS hodnoceni (
        id PRIMARY KEY,
        nazev_filmu TEXT,
        hodnoceni INTEGER
    )
    """
)

# Hodnocení: u primary key chybí datový typ

# Zapsání do databáze

cursor.execute(
    "INSERT INTO hodnoceni (id, nazev_filmu, hodnoceni) VALUES (1, 'kamenak', '8')"
)

# Hodnocení: -10 bodů za příliš kladné hodnocení Kameňáku

connection.commit()


# Vypisování hodnocení

cursor.execute("SELECT * FROM hodnoceni")

rows = cursor.fetchall()

print("hodnoceni :", rows[0][2])

connection.close()
