# import the order module automatically
import sales
from sales.order import create_sales_order

# default sales tax rate
TAX_RATE = 0.07
sales.order.create_sales_order()