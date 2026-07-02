item_1 = "laptop"
laptop_price = 5000
laptop_quantity = 2

item_2 = "USB_CABLE"
usb_cable_price = 500
usb_cable_quantity = 2

item_3 = "mouse_pad"
mouse_pad_price = 300
mouse_pad_quantity = 2



print("------------ Reciept -----------")
print(f"{item_1 :<5} x{laptop_quantity}     @ ${laptop_price:<20.2f} = {laptop_price*laptop_quantity:.2f}")
print(f"{item_2 :<5} x{usb_cable_quantity}  @ ${usb_cable_price:<20.2f} = {usb_cable_price*usb_cable_quantity:.2f}")
print(f"{item_3 :<5} x{mouse_pad_quantity}  @ ${mouse_pad_price:<20.2f} = {mouse_pad_price*mouse_pad_quantity:.2f}")


print('-----------'*4)




total = laptop_price*laptop_quantity + usb_cable_price*usb_cable_quantity+ mouse_pad_quantity*mouse_pad_price
discount = 0
if total > 50:
    discount = total * (10/100)
    final_price = total - discount
else :
    final_price = total



print(f"subtotal:     ${total:.2f}")
print(f"discount:   - ${discount:.2f}")
print(f"Final price:  ${final_price:.2f}")