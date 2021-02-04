import sqlite3
import gzip

if __name__ == "__main__":
    conn = sqlite3.connect("MEta/ORID.sqlite")
    conn.execute("UPDATE rid SET State=1")
    conn.commit()
    conn.close()
    gzip.open("Data/rest.jl.gz", "wb+").close()
    gzip.open("Data/review.jl.gz", "wb+").close()
    print("Spider reset.")
