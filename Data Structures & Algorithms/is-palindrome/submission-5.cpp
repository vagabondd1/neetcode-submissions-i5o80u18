class Solution {
public:
    bool isPalindrome(string s) {
        size_t left, right;
        string lower_s = "";

        for (char el: s) {
            if (isalnum(el)) {
                lower_s += tolower(el);
            }
        }

       if (lower_s.size() == 0 || lower_s.size() == 1) return true;

        left = 0;
        right = lower_s.size() - 1;

        for (size_t i = 0; i <= (left + right) / 2; ++i) {
            if (lower_s[left + i] != lower_s[right - i]) {
                return false;
            }
        }
        return true;
    }
};