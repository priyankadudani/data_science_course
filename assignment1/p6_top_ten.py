import sys
import json
import heapq
    
def main():    
    tweet_file = open(sys.argv[1])
    freq = {};  #"word" : "freq"
    while True:
        line = tweet_file.readline()
        if not line:
            break
        dict = json.loads(line);
        hashtag_list = dict["entities"]["hashtags"];
        
        for hashtag in hashtag_list:
            word = hashtag["text"];
            if freq.has_key(word):
                f = int(freq[word]) + 1;
                freq[word] = f;
            else:
                freq[word] = 1;

    popular_words = sorted(freq, key = freq.__getitem__, reverse = True)
    top_ten = popular_words[:10];
    
    for top_elem in sorted(top_ten, key = freq.__getitem__, reverse = False):
        print top_elem, float(freq[top_elem]);
    
if __name__ == '__main__':
    main()