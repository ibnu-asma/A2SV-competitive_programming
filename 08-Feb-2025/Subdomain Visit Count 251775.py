# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_counts = {}
        for item in cpdomains:
            cp, domain = item.split()
            cp = int(cp)
            domain_list = domain.split(".")

            for i in range(len(domain_list)):
                subdomain = ".".join(domain_list[i:])
                domain_counts[subdomain] = domain_counts.get(subdomain, 0) + cp

        result = []
        for domain, count in domain_counts.items():
            result.append(str(count) + " " + domain)
        return result