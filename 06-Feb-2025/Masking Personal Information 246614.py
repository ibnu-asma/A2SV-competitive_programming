# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        print(type("*" * 4))
        if '.' in s:
            index_of_at = s.index('@')
            name = s[:index_of_at].lower()
            domain = s[index_of_at + 1:].lower()
            return name[0]+ "".join("*****") + name[-1] + '@' + domain
        else:
            cleaned_phone_number =  ""
            result = ""
            special_character = {'+', '-', '(', ')', ' '}
            for num in s:
                if num in special_character:
                    continue
                cleaned_phone_number += num
            mask = "".join("***-")
            result =  mask + mask + cleaned_phone_number[-4:]
            if len(cleaned_phone_number) == 10:
                return result
            else:
                country_code_mask = "*" * (len(cleaned_phone_number) % 10)
                return ('+' + country_code_mask + '-' + result)
                