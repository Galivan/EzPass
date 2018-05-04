import Definitions
import DbManager
import sqlite3



def main():
    print(Definitions.DB_PATH)
    conn = sqlite3.connect(Definitions.DB_PATH)
    print(conn)


if __name__ == '__main__':
    main()
