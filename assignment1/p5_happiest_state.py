import sys
import json

def getTermScores(fileName):
    afinnfile = open(fileName);
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
      
    return scores # return every (term, score) pair in the dictionary
    
def main():
    #sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = getTermScores(sys.argv[1]);
    states = {};
    
    while True:
        line = tweet_file.readline();
        if not line:
            break
        dict = json.loads(line);
        
        if "place" in dict.keys() and dict["place"] is not None:
            place = dict["place"];
            #if dict["lang"] == "en" and place["country_code"] == "US":
            if place["country_code"] == "US":
                text = dict["text"];
                tweet_score = 0;
                for word in text.split():
                    if scores.has_key(word):
                        tweet_score = tweet_score + int(scores[word]);
                #print tweet_score;
                fullName = place["full_name"].upper();
                state = fullName[-2:];
                #print state;
                if states.has_key(state):
                    val = states[state]
                    val = val + tweet_score;
                    states[state] = val;
                else :
                    states[state] = tweet_score;
        
    if len(states):
        happiest_state = max(states, key=states.__getitem__);
        print happiest_state;
        
if __name__ == '__main__':
    main()
