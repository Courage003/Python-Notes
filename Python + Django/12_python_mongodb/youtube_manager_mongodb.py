from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://youtubepy:youtubepy@youtube-manager.e6ahl0o.mongodb.net/", tlsAllowInvalidCertificates = True)
#Not a good idea to include id and password in code files
#Not a good way to handle SSl

db = client["Youtube-Manager"]
video_collection = db["videos"]


print(video_collection)

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']} and Time: {video['time']} ")


def update_video(id, new_name, new_time):
    video_collection.update_one(
        {'_id': ObjectId (id)},
        {"$set": {"name": new_name, "time": new_time}}
    )

def delete_video(id):
    video_collection.delete_one({"_id": id})

#ToDO debug id problem
def main():
    while True:
        print("\n Youtube Manager | Choose an option ")
        print("1. List a favourite video ")
        print("2. Add a Youtube video ")
        print("3. Update a Youtube video details ")
        print("4. Delete a Youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")
        if choice == '1':
            list_videos()

        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)

        elif choice == '3':
            id = input("Enter id to update: ")
            name = input("Enter updated video name: ")
            time = input("Enter updated video time: ")
            update_video(id, name, time)

        elif choice == '4':
            id = input("Enter id to delete: ")
            delete_video(id)

        elif choice == '5':
            break

        else:
            print("Invalid Choice")    






if __name__ == "__main__":
    main()



#Read more about bson 
# #check about id problems and issues here
#     