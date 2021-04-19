import pymongo
import datetime


class Mongo_Client(object):
    def __init__(self):
        self.mongo_url = pymongo.MongoClient("mongodb://localhost:27017/")
        self.my_db = self.mongo_url["Audio_Files"]
        self.collection = self.my_db["song_files"]

    def get_file(self, uid):
        conn = self.collection.find_one()
        for conn in self.collection.find():
            print(conn)
        return conn

    def add_file(self, payload):
        print(payload)
        if payload['audioFileType'] == "song_file":
            song_metadata = payload["audioFileMetadata"]
            if song_metadata["track_title"] and len(song_metadata["track_title"]) <= 100:
                track_title = song_metadata["track_title"]
            else:
                return "track title is not present in the song file"

            if song_metadata["duration"] and str(type(song_metadata["duration"])) == "<class 'int'>":
                duration = song_metadata["duration"]
            else:
                return "duration is not present in the song file"

            uploaded_date_time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            highest_uid = self.collection.find_one(sort=[("uid", -1)])
            print("highest_uid",highest_uid)
            if not highest_uid:
                track_uid = 1
            else:
                track_uid = highest_uid['uid'] + 1

            if song_metadata['artist']:
                artist = song_metadata['artist']
            else:
                artist = ""
            if song_metadata['album']:
                album = song_metadata['album']
            else:
                album = ""
            if song_metadata['genre']:
                genre = song_metadata['genre']
            else:
                genre = ""
            input_data = {"uid": track_uid, "Artist": artist, "Album": album, "Track title": track_title,
                          "Genre": genre, "Duration": duration, "uploaded_time": uploaded_date_time}
            conn = self.collection.insert_one(input_data)
            return "success"


"""obj = Mongo_Client()
resp = obj.add_file({
    "audioFileType": "song_file",
    "audioFileMetadata": {
        "artist": "Artist",
        "album": "Album",
        "track_title": "Track title",
        "genre": "Genre",
        "duration": 302
    }
})
print(resp)"""