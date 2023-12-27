import telebot
from telebot import types
from database import Database
from keys import token, admin_id

bot = telebot.TeleBot(token)
db = Database()

@bot.message_handler(commands=['add_today_stats'])
def add_today_stats(message):
    user_id = message.from_user.id

    if user_id == admin_id:
        markup = types.ForceReply(selective=False)
        bot.send_message(user_id, "Vvedite segodnyashniy doxod:", reply_markup=markup)
        bot.register_next_step_handler(message)
    else:
        bot.send_message(user_id, "Izvinite, vy ne admin.")



def process_earnings(message):
    try:
        earnings = float(message.text)
        date = message.date
        earn_usd = earnings / 10500  
        db.add_statistics(date, earnings, earn_usd)

        bot.send_message(admin_id, f"Zapis dobavlena v bazу: {date}, UZS: {earnings}, USD: {earn_usd}")
    except ValueError:
        bot.send_message(admin_id, "nevernaya summa")

if __name__ == "__main__":
    bot.polling(none_stop=True)
