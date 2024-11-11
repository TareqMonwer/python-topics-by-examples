We browse catalogue.
We select and add item to cart (item has qty, variation, price, total price).
Cart gets updated as we add items to cart (cart has total items/rows, total price, tax, vat, coupon/discount).


ShoppingCartSystem:
  add_to_cart:
  remove_cart_item:
  update_cart_item_details:
  get_pricing_summary:
  get_cart_price:


CartRow:
  get_qty:
  update_qty:
  update_variation:
  get_total_price:

Cart:
  add_to_cart:
  get_total_price:
