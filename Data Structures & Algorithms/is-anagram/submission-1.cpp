class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char,int> hash;
        for (auto el : s) {
            hash[el] += 1;
        }
    
        for (auto el : t) {
            hash[el] -= 1;
            if (hash[el] < 0) {
                return false;
            }
        }

        for (auto pair : hash) {
            if (hash[pair.first] != 0) return false;
        }
        return true;
    }
};