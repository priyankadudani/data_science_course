import sys
import json

def getTermScores(fileName):
    afinnfile = open(fileName);
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
    
    return scores # return every (term, score) pair in the dictionary

def hw():
    print 'Hello, world!';
    
def lines(fp):
    print str(len(fp.readlines()));
    
def main():
    #sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    scores = getTermScores(sys.argv[1]);
    while True:
        line = tweet_file.readline()
        if not line:
            break
        dict = json.loads(line);
        text = dict["text"];
        tweet_score = 0;
        for word in text.split():
            if scores.has_key(word):
                tweet_score = tweet_score + int(scores[word]);
        print tweet_score;
    
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
