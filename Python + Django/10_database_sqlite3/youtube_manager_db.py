import sqlite3

conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )
''')


def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?) ", (name, time))
    conn.commit()


def update_video(id, new_name, new_time):

    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, id))
    conn.commit()

def delete_video(id):
    cursor.execute("DELETE FROM videos where id = ?", (id,))
    conn.commit()




def main():
    while True:
        print("\n Youtube Manager | Choose an option ")
        print("1. List a favourite video ")
        print("2. Add a Youtube video ")
        print("3. Update a Youtube video details ")
        print("4. Delete a Youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")
        #print(videos)

        if choice == '1':
            list_videos()

        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)

        elif choice == '3':
            id = input("Enter video ID to update: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(id, name, time)    

        elif choice == '4':
            id = input("Enter video ID to delete: ")
            
            delete_video(id)      

        elif choice == '5':
            break

        else:
            print("Invalid Choice")
    
    conn.close()  #to free memory and saving db from getting corrupted



if __name__ == "__main__":
    main()
