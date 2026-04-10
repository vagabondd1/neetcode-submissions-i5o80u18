class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        vector<int> mass;
        for (auto el : nums) {
            if (find(mass.begin(),mass.end(), el) != mass.end()) {
                return true;
            }
            mass.push_back(el);
        }
        return false;
    }
};