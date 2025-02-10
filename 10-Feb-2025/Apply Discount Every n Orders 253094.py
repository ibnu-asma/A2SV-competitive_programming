# Problem: Apply Discount Every n Orders - https://leetcode.com/problems/apply-discount-every-n-orders/description/

class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.product_price = {}
        for i in range(len(products)):
            self.product_price[products[i]] = prices[i]
        self.customers = 0
        

    def getBill(self, product: List[int], amount: List[int]) -> float:
        total = 0
        for i in range(len(product)):
            product_id = product[i]
            quantity = amount[i]
            total += self.product_price[product_id] * quantity

        self.customers += 1
        if self.customers % self.n == 0:
            total *= ((100 - self.discount) / 100)
        return total
        
# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)


