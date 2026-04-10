class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
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
        return true;
    }
};