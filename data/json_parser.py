"""
json_parser.py
Reads json files of Spotify data
"""


import json


def read_file():
    # with open('sample.json', 'r') as sample_file:
    #     sample_dict = json.load(sample_file)
    
    # for item in sample_dict:
    #     year, month = item['endTime'][0:4], item['endTime'][5:7]
    #     artist, track, ms = item['artistName'], item['trackName'], item['msPlayed']
    #     print(f'{year},{month},{artist},{track},{ms}')
    # sample_file.close();

    with open('../../../../Documents/Spotify/MyData/StreamingHistory4.json', 'r') as main_file:
        main_dict = json.load(main_file)
    
    for item in main_dict:
        year, month, day = item['endTime'][0:4], item['endTime'][5:7], item['endTime'][8:10]
        artist, track, ms = item['artistName'], item['trackName'], item['msPlayed']
        print(f'{year},{month},{day},{artist},{track},{ms}')
    main_file.close();


# read_file()

if __name__ == "__main__":
    read_file()
    # print(read_file)