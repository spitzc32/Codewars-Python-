def discover_original_price(discounted_price, sale_percentage):
    return round(discounted_price / ((100 - sale_percentage) * 0.01), 2)

# Another solution
def discover_original_price(discounted_price, sale_percentage):
    sale_per_dec = float('.' + str(sale_percentage).replace('.','')) if sale_percentage > 10 else float('.0' + str(sale_percentage).replace('.','')) 
    return round(discounted_price / (1 - sale_per_dec), 2)