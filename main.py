import telebot
import copy
from telebot import types

# Set up the bot
bot = telebot.TeleBot("6101915824:AAGJdeUXTLcEl5iVvfc79vFw-iUZvP7CHA4")
admin_id = "5807502330"

# Set up the inventory
inventory = {
  1: {
    "name": "Milk",
    "Brand": "Aavin",
    "Weight": "500 ml",
    "price": 40,
    "stock": 10,
    "description": "Fresh Aavin Full Cream Milk from Aavin Booth ",
    "image_url":
    "https://www.aavinkanyakumari.com/assets/images/product/m1.jpg"
  },
  2: {
    "name":
    "Bread",
    "Brand":
    "Modern",
    "Weight":
    "450 g",
    "price":
    30,
    "stock":
    50,
    "description":
    "Modern Sandwich Bread for making delicious sandwiches.",
    "image_url":
    "https://ik.imagekit.io/dunzo/1614936650616_variant_5d76270e4bf1844dbc4ec98a_1.jpg?tr=w-436,h-436,cm-pad_resize"
  },
  3: {
    "name":
    "Chips",
    "Brand":
    "Bingo",
    "Weight":
    "25 g",
    "price":
    10,
    "stock":
    100,
    "description":
    "A new flavor of the Bingo Potato chips this time with chilly sprinkled.",
    "image_url":
    "https://www.bigbasket.com/media/uploads/p/xxl/1204088-2_3-bingo-yumitos-potato-chips-original-style-chilli.jpg"
  },
  4: {
    "name": "Detergent",
    "Brand": "Ariel",
    "Weight": "500 ml",
    "price": 250,
    "stock": 20,
    "description":
    "Ariel detergent value pack for both Semi-Auto and Hand Wash",
    "image_url": "https://m.media-amazon.com/images/I/71QOZO95pQL._SL1500_.jpg"
  },
  5: {
    "name":
    "Butter",
    "Brand":
    "Amul",
    "Weight":
    "500 g",
    "price":
    97,
    "stock":
    25,
    "description":
    "Amul Pasteurised Butter for cooking purposes.",
    "image_url":
    "https://www.jiomart.com/images/product/600x600/490001392/amul-butter-500-g-carton-product-images-o490001392-p490001392-6-202203152128.jpg"
  },
  6: {
    "name": "Repellent",
    "Brand": "Odomos",
    "Weight": "500 ml",
    "price": 150,
    "stock": 25,
    "description": "Odomos Naturals Mosquitto Repellent Spray-Safe for skin",
    "image_url": "https://m.media-amazon.com/images/I/610qQ1wVFfL._SL1500_.jpg"
  },
  7: {
    "name":
    "Cookies",
    "Brand":
    "UNIBIC",
    "Weight":
    "50 g",
    "price":
    25,
    "stock":
    100,
    "description":
    "UNIBIC Choco Chip Cookies ",
    "image_url":
    "https://www.bigbasket.com/media/uploads/p/xxl/267154_3-unibic-cookies-chocolate-chip.jpg"
  },
  8: {
    "name":
    "Rice",
    "Brand":
    "India Gate",
    "Weight":
    "1 Kg",
    "price":
    200,
    "stock":
    50,
    "description":
    "India Gate Basmati Rice Tibar",
    "image_url":
    "https://asset20.ckassets.com/blog/wp-content/uploads/sites/5/2021/12/India-Gate-Rice-1024x512.jpg"
  },
  9: {
    "name":
    "Eggs",
    "Brand":
    "Eggee",
    "Weight":
    "250 g",
    "price":
    50,
    "stock":
    150,
    "description":
    "Eggee Provilla5 Brown Eggs ",
    "image_url":
    "https://www.bigbasket.com/media/uploads/p/l/40187132_1-eggee-brown-eggs.jpg"
  },
  10: {
    "name":
    "Juice",
    "Brand":
    "Real",
    "Weight":
    "500 ml",
    "price":
    56,
    "stock":
    50,
    "description":
    "Real Mixed Fruit Juice Can - Rich in Vitamin C ",
    "image_url":
    "https://www.bigbasket.com/media/uploads/p/xxl/229922_5-real-fruit-power-juice-mixed.jpg"
  }
}
old_inventory = copy.deepcopy(inventory)
# Set up the orders dictionary
orders = {}
pending_orders = {}
status = {}


# Handle the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
  welcome_message = "Welcome to the 24/7 general store bot. Here is a list of available items and their prices:\n\n"

  # Create the table header
  table_header = "ID  | Name              |  Price           |  Stock\n"
  table_header += "-" * len(table_header) + "\n"

  # Create the table body
  table_body = ""
  for item_id, item_info in inventory.items():
    table_body += f"{item_id:<4} | {item_info['name']:<20}|Rs{item_info['price']:<6.2f}      | {item_info['stock']}\n"

  # Combine the table and welcome message
  welcome_message += table_header + table_body
  welcome_message += "\nType /catalogue to display the catalogue,\n/add <item number> <quantity> to add an item to your cart,\n/item <item number> to know more details about the item (Brand name, weight,stock,etc..), \n/cart to view your cart,\n/removeitem <item number> [<quantity>] to remove an item from cart,\n/placeorder to place your order,or \n/rating to rate your experience after ordering"

  bot.reply_to(message, welcome_message)


# Handle the /catalogue command
@bot.message_handler(commands=['catalogue'])
def display_catalogue(message):
  catalogue_message = "Here is a list of available items and their prices:\n\n"
  for item_id, item_info in inventory.items():
    catalogue_message += f"{item_id}. {item_info['name']} - Rs{item_info['price']:.2f} (Stock: {item_info['stock']})\n"
  bot.reply_to(message, catalogue_message)


# Handle the /item command
@bot.message_handler(commands=['item'])
def show_item(message):
  try:
    args = message.text.split()
    item_number = int(args[1])
    item = inventory.get(item_number)
    if item is None:
      bot.reply_to(message, "Invalid item number.")
    else:
      response = f"\n{item['name']}\nBrand:  {item['Brand']} \nWeight:  {item['Weight']} \nPrice:  Rs.{item['price']}\nStock:  {item['stock']}\nDescription:  {item['description']}"
      bot.reply_to(message, response)
      bot.send_photo(message.chat.id, item['image_url'])

  except:
    bot.reply_to(message, "Invalid command. Please type /item <item number>.")


# Handle the /order command
@bot.message_handler(commands=['add'])
def order_item(message):
  try:
    args = message.text.split()
    item_number = int(args[1])
    quantity = int(args[2]) if len(args) > 2 else 1
    item = inventory.get(item_number)
    if item is None:
      bot.reply_to(message, "Invalid item number.")
    else:
      if item['stock'] < quantity:
        bot.reply_to(
          message,
          f"Sorry, there is not enough stock of {item['name']}. Please add another item"
        )
      else:
        user_id = message.chat.id
        if user_id not in orders:
          orders[user_id] = []
        found_item = False
        for i, (cart_item, cart_quantity) in enumerate(orders[user_id]):
          if cart_item == item:
            orders[user_id][i] = (item, cart_quantity + quantity)
            found_item = True
            break
        if not found_item:
          orders[user_id].append((item, quantity))
        item['stock'] -= quantity
        bot.reply_to(
          message,
          f"{quantity}x {item['name']} added to cart.\nUse /cart to view the items in the cart."
        )
  except:
    bot.reply_to(
      message, "Invalid command. Please type /add <item number> [quantity].")


# Handle the /removeitem command
@bot.message_handler(commands=['removeitem'])
def remove_item(message):
  try:
    args = message.text.split()
    item_number = int(args[1])
    quantity = int(args[2]) if len(args) > 2 else 1
    item = inventory.get(item_number)
    if item is None:
      bot.reply_to(message, "Invalid item number.")
    else:
      user_id = message.chat.id
      if user_id not in orders:
        bot.reply_to(message, "Your cart is empty.")
      else:
        found_item = False
        for i, (cart_item, cart_quantity) in enumerate(orders[user_id]):
          if cart_item == item:
            found_item = True
            if cart_quantity < quantity:
              # orders[user_id].pop(i)
              cart_message = f"Not enough {item['name']}(s) in cart."
              quantity = 0
            elif cart_quantity == quantity:
              orders[user_id].pop(i)
              cart_message = f"{item['name']} removed from cart.\nView /cart to see the updated items in the cart."
            else:
              orders[user_id][i] = (item, cart_quantity - quantity)
              cart_message = f"{quantity}x {item['name']} removed from cart.\nView /cart to see the updated items in the cart."
            item['stock'] += quantity

            if len(orders[user_id]) == 0:
              del orders[user_id]

            bot.reply_to(message, cart_message)
            break
        if not found_item:
          bot.reply_to(message, f"{item['name']} not found in your cart.")
  except:
    bot.reply_to(
      message,
      "Invalid command. Please type /removeitem <item number> [quantity].")


# Handle the /cart command
@bot.message_handler(commands=['cart'])
def show_cart(message):
  user_id = message.chat.id
  if user_id not in orders:
    bot.reply_to(message, "Your cart is empty.")
  else:
    cart_items = []
    for item, quantity in orders[user_id]:
      cart_items.append(f"{quantity}x {item['name']}")
    cart_summary = "\n".join(cart_items)
    bot.reply_to(
      message,
      f"Your cart contains:\n\n{cart_summary}\n\nType /add to add more items to your cart or type /placeorder to place your order."
    )


@bot.message_handler(commands=['placeorder'])
def place_order(message):
  user_id = message.chat.id
  if user_id in pending_orders:
    bot.reply_to(
      message,
      "You have a pending order, please wait for it to be accepted before placing another order."
    )

  elif user_id not in orders:
    bot.reply_to(
      message,
      "Your cart is empty. Please add items to your cart to place an order.")
  else:
    items = orders[user_id]
    total_cost = sum(item['price'] * quantity for item, quantity in items)
    order_message = f"Your Cart:\n\n"
    for item, quantity in items:
      order_message += f"{item['name']} - Rs {item['price']:.2f} x {quantity}\n"
    order_message += f"Total cost: Rs {total_cost:.2f}\n\nHow would you like to receive your order?\n1. Pickup\n2. Home Delivery\n\nPlease select an option by typing '1' for Pickup or '2' for Delivery."
    bot.send_message(chat_id=user_id, text=order_message)
    bot.register_next_step_handler(message, process_order_delivery)


def process_order_delivery(message):
  user_id = message.chat.id
  delivery_option = message.text.lower()
  if delivery_option == '1':
    confirm_pickup_order(message)
  elif delivery_option == '2':
    bot.send_message(chat_id=user_id,
                     text="Please enter your delivery address:")
    bot.register_next_step_handler(message, process_order_address)
  else:
    bot.send_message(
      chat_id=user_id,
      text=
      "Invalid input. Please type /placeorder to choose your mode of receiving order."
    )


def process_order_address(message):
  user_id = message.chat.id
  delivery_address = message.text

  items = orders[user_id]
  total_cost = sum(item['price'] * quantity for item, quantity in items)
  order_message = f"Review order:\n\n"
  for item, quantity in items:
    order_message += f"{item['name']} - Rs {item['price']:.2f} x {quantity}\n"

  order_message += f"\nTotal cost: Rs {total_cost:.2f}\n\nDelivery option: Home Delivery\nDelivery address: {delivery_address}\n\nDo you wish to confirm your order ? type 'yes' or 'no'"

  bot.send_message(chat_id=user_id, text=order_message)
  bot.register_next_step_handler(message, confirm_delivery,
                                 {'address': delivery_address})


def confirm_delivery(message, data):
  user_id = message.chat.id

  items = orders[user_id]

  confirmation = message.text.lower()
  if (confirmation == 'yes'):

    status[user_id] = 'delivery'

    delivery_address = data['address']
    total_cost = sum(item['price'] * quantity for item, quantity in items)
    order_message = f"New order from user {user_id}:\n\n"
    for item, quantity in items:
      order_message += f"{item['name']} - Rs {item['price']:.2f} x {quantity}\n"
    order_message += f"\nTotal cost: Rs {total_cost:.2f}\n\nDelivery option: Home Delivery\nDelivery address: {delivery_address}\n\nYou can now use /accept <user_id> or /decline <user_id> to accept or decline the order respectively."

    confirmation_message = f"Order sent to store owner, wait for confirmation .\n"
    bot.send_message(chat_id=user_id, text=confirmation_message)
    bot.send_message(chat_id=admin_id, text=order_message)
    pending_orders[user_id] = copy.copy(orders[user_id])
    del orders[user_id]
  else:
    bot.send_message(
      chat_id=user_id,
      text="Your order has been cancelled. You may continue shopping.")


def confirm_pickup_order(message):
  user_id = message.chat.id
  items = orders[user_id]
  total_cost = sum(item['price'] * quantity for item, quantity in items)
  order_message = f"Review order:\n\n"
  for item, quantity in items:
    order_message += f"{item['name']} - Rs {item['price']:.2f} x {quantity}\n"
  order_message += f"Total cost: Rs {total_cost:.2f}\n\nDelivery option: Pickup\n\nWould you like to confirm the order?\nPlease type 'yes' or 'no'."
  bot.send_message(chat_id=user_id, text=order_message)
  bot.register_next_step_handler(message, process_order_confirmation)


def process_order_confirmation(message):
  user_id = message.chat.id
  confirmation = message.text.lower()
  if confirmation == 'yes':

    status[user_id] = 'pickup'

    items = orders[user_id]
    total_cost = sum(item['price'] * quantity for item, quantity in items)
    order_message = f"New order from user {user_id}:\n\n"
    for item, quantity in items:
      order_message += f"{item['name']} - Rs {item['price']:.2f} x {quantity}\n"
    order_message += f"\nTotal cost: Rs {total_cost:.2f}\n\nDelivery option: Pickup\n\n\n You can now use /accept <user_id> or /decline <user_id> to accept or decline the order respectively."
    bot.send_message(chat_id=admin_id, text=order_message)
    bot.send_message(chat_id=user_id,
                     text="Order sent to store owner, wait for confirmation")
    pending_orders[user_id] = copy.copy(orders[user_id])
    del orders[user_id]
  elif confirmation == 'no':
    bot.send_message(
      chat_id=user_id,
      text="Your order has been cancelled. You may continue shopping.")
  else:
    bot.send_message(chat_id=user_id,
                     text="Invalid input. Please type 'yes' or 'no'.")


import qrcode


# Handle the /accept command
@bot.message_handler(commands=['accept'])
def accept_order(message):
  if message.chat.id != int(admin_id):
    bot.reply_to(message, "You are not authorized to use this command.")
    return

  try:
    user_id = int(message.text.split()[1])
    if user_id not in pending_orders:
      bot.reply_to(message, "No order found for this user.")
    else:
      items = pending_orders[user_id]
      total_cost = sum(item['price'] * quantity
                       for item, quantity in pending_orders[user_id])

      # total_cost = sum(item['price'] for item in items)
      item_list = ""
      for item, quantity in items:
        item_list += f"{item['name']} - Rs {item['price']:.2f} x {quantity}\n"
      order_message = f"Order accepted for user {user_id}:\n" + item_list + f"Total cost: Rs {total_cost:.2f}"

      # Create QR code for payment
      qr = qrcode.QRCode(version=1,
                         error_correction=qrcode.constants.ERROR_CORRECT_L,
                         box_size=10,
                         border=4)
      qr.add_data(
        f"upi://pay?pa=psvarsha2002@okaxis&pn=Store%20Name&tr=1234ABCD&am={total_cost}&cu=INR"
      )
      qr.make(fit=True)
      img = qr.make_image(fill_color="black", back_color="white")
      img.save("payment_qr.png")

      # Send payment QR code to user

      if (status[user_id] == 'delivery'):
        bot.send_photo(chat_id=user_id, photo=open("payment_qr.png", "rb"))

        bot.send_message(
          chat_id=user_id,
          text=
          "Thank You for shopping with us!! Your order has been accepted by the store. We'll deliver your order in 10 minutes.\n"
          "Scan the QR code to make payment on delivery.")
      else:
        bot.send_message(
          chat_id=user_id,
          text=
          "Thank You for shopping with us!! Your order has been accepted by the store. Your order will be ready for pickup in 10 minutes.\n"
        )

      bot.send_message(
        chat_id=user_id,
        text=
        "For any further queries regarding your order please contact the store owner. contact no: 9568919865",
      )

      bot.send_message(
        chat_id=user_id,
        text="Kindly type /rating to rate your experience",
      )

      bot.send_message(chat_id=admin_id, text=order_message)
      del pending_orders[user_id]
      del status[user_id]
  except:
    bot.reply_to(message, "Invalid command. Please type /accept <user_id>.")


# create a handler for the rating command
@bot.message_handler(commands=['rating'])
def rating_handler(message):
  # create a new inline keyboard
  markup = types.InlineKeyboardMarkup()

  # add rating options to the keyboard
  markup.add(types.InlineKeyboardButton(text='😠', callback_data='1'),
             types.InlineKeyboardButton(text='😞', callback_data='2'),
             types.InlineKeyboardButton(text='😕', callback_data='3'),
             types.InlineKeyboardButton(text='🙂', callback_data='4'),
             types.InlineKeyboardButton(text='😊', callback_data='5'))

  # send the rating prompt message with the inline keyboard
  bot.send_message(chat_id=message.chat.id,
                   text='How was your experience with our telebot?',
                   reply_markup=markup)


# create a handler for the callback data from the rating keyboard
@bot.callback_query_handler(func=lambda call: True)
def rating_callback_handler(call):
  # get the rating value from the callback data
  rating = int(call.data)

  # send a message to thank the user for their feedback
  bot.send_message(
    chat_id=call.message.chat.id,
    text=
    f'Thank you for your {rating} star rating!. We appreciate your feedback 😊')


# Handle the /decline command
@bot.message_handler(commands=['decline'])
def decline_order(message):

  if message.chat.id != int(admin_id):
    bot.reply_to(message, "You are not authorized to use this command.")
    return
  try:
    user_id = int(message.text.split()[1])
    if user_id not in pending_orders:
      bot.reply_to(message, "No order found for this user.")
    else:
      items = pending_orders[user_id]
      item_list = ""
      for item, quantity in items:
        item['stock'] += quantity
        item_list += f"{item['name']} - x{quantity}\n"
      bot.send_message(
        chat_id=user_id,
        text=
        "Sorry, Your order has been declined by the store owner. You may continue shopping "
      )
      bot.send_message(chat_id=admin_id,
                       text=f"Order declined for user {user_id}:\n" +
                       item_list)
      del pending_orders[user_id]
  except:
    bot.reply_to(message, "Invalid command. Please type /decline <user_id>.")


# Handle the /admin command
@bot.message_handler(commands=['admin'])
def change_admin_id(message):

  try:
    password = message.text.split()[1]
    if password == "mypassword":
      # new_admin_id = message.chat.id
      global admin_id
      admin_id = str(message.chat.id)
      bot.reply_to(
        message,
        f"Admin ID changed to {admin_id}.\nYou can now accept or decline orders using commands /accept <user id> or /decline <user id> respectively "
      )
    else:
      bot.reply_to(message, "Invalid password. Please try again.")
  except IndexError:
    bot.reply_to(message,
                 "Invalid command format. Please type /admin <password>.")


@bot.message_handler(commands=['restore'])
def restore_stock(message):
  user_id = str(message.chat.id)
  global inventory
  if (user_id == "5807502330"):
    inventory = copy.deepcopy(old_inventory)
    bot.reply_to(message, "stock restored")
  else:
    bot.reply_to(message, "you are not authorized")


bot.polling()
