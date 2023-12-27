import telebot
from telebot import types
from keys import token, admin_id

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['add_today_stats'])
def add_today_stats(message):
    user_id = message.from_user.id

    if user_id == admin_id:
        markup = types.ForceReply(selective=False)
        bot.send_message(user_id, "Vvedite segodnyashniy doxod:", reply_markup=markup)
        bot.register_next_step_handler(message)
    else:
        bot.send_message(user_id, "Izvinite, vy ne admin.")


if __name__ == "__main__":
    bot.polling(none_stop=True)
