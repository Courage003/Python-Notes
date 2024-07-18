import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file) 

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        
        print(f" {index}. {video['name']}, Duration: {video['time']} ")
    print("\n")
    print("*" * 70)

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video duration: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    id = int(input("Enter the video number to update "))
    if 1<= id <= len(videos):
        name = input("Enter the video name")
        time = input("Enter the video time")
        videos[id-1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid id selected")

def delete_video(videos):
    list_all_videos(videos)
    id = int(input("Enter the video number to delete "))
    if 1<= id <= len(videos):
        del videos[id-1]
        save_data_helper(videos)
    else:
        print("Invalid video id selected")    

def main():
    #shortcut key for group indentation 'ctrl + ]'

    videos = load_data()
    while True:
        print("\n Youtube Manager | Choose an option ")
        print("1. List a favourite video ")
        print("2. Add a Youtube video ")
        print("3. Update a Youtube video details ")
        print("4. Delete a Youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")
        #print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)    
            case '4':
                delete_video(videos)    
            case '5':
                break
            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()
