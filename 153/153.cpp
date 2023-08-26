#include <iostream>
#include <string>
using namespace std;

// Find an efficient algorithm to find the smallest distance (measured in number of words)
// between any two given words in a string.

// For example, given words "hello", and "world" and a text content
// of "dog cat hello cat dog dog hello cat world", return 1 because
//  there's only one word "cat" in between the two words.

int main()
{
    // parameters
    string input = "world d hello d d world d d d d d hello d d d d d world d d hello";
    string word1 = "hello";
    string word2 = "world";

    // working variables
    string word = "", first = "", second = "";
    int iterr = 0, pos = 0, pos1 = 0, pos2 = 0;
    bool runLogic = false, pos2Set = false;
    int best = 10000;

    // main logic
    input += " ";
    while (iterr < input.size())
    {
        if (input[iterr] != ' ')
        {
            word += input[iterr];
        }
        else
        { // word fully parsed, set accordingly
            // run logic if one of the words are word1 or word2
            if (word == word1)
            {
                first = word;
                pos1 = pos;
                runLogic = true;
            }
            else if (word == word2)
            {
                second = word;
                pos2 = pos;
                pos2Set = true; // do not touch, very farrrrr edge case
                runLogic = true;
            }
            else
            {
                runLogic = false;
            }

            if (runLogic && pos2Set)
            {
                // if first word before second word
                if ((pos2 - pos1) > 0 && (pos2 - pos1) < best)
                {
                    best = (pos2 - pos1) - 1;
                    if (pos1 < pos2)
                    {
                        first = "";
                    }
                    else
                    {
                        second = "";
                    }
                } // if second word before first word
                else if ((pos2 - pos1) < 0 && abs(pos2 - pos1) < best)
                {
                    best = abs(pos2 - pos1) - 1;
                    if (pos1 < pos2)
                    {
                        first = "";
                    }
                    else
                    {
                        second = "";
                    }
                }
            }
            pos++;
            word = "";
        }
        iterr++;
    }

    cout << "Lowest combination is --> " << best;
    return 0;
}
