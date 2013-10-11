import sys
import json
    
def main():    
    tweet_file = open(sys.argv[1])
    all_word_count = 0;
    freq = {};  #"word" : "freq"
    while True:
        line = tweet_file.readline()
        if not line:
            break
        dict = json.loads(line);
        text = dict["text"];
        for word in text.split():
            all_word_count = all_word_count + 1;
            if freq.has_key(word):
                f = int(freq[word]) + 1;
                freq[word] = f;
            else:
                freq[word] = 1;

    for w in freq.keys():
        val = freq[w]/float(all_word_count);
        #print val;
        print w + " " + str(val);
        
if __name__ == '__main__':
    main()
