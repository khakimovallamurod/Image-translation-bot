from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CallbackContext
import keyboards
import db
import time

def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    update.message.reply_text(
        text=f"""Assalomu aleykum {user.full_name}. To'plamdan birontasini tanlang""",
        reply_markup=keyboards.home_keyboard()
    )

def contact(update: Update, context: CallbackContext):
    user = update.message.from_user
    update.message.reply_contact(
        phone_number="+998938554640",
        first_name="Xakimov Allamurod",
        reply_markup=keyboards.home_keyboard()
    )


def models(update: Update, context: CallbackContext):
    user = update.message.from_user
    update.message.reply_text(
        text=f"{user.full_name} let is start!",
        reply_markup=keyboards.models_keyboard()
    )

def one_model(update: Update, context: CallbackContext):
    ml = update.callback_query.data.split(":")[1]
    text = db.get_one_model(ml)
    for item in text:
        sent_message  = update.callback_query.message.reply_photo(
            photo=item['img_url'],
            caption='Rasmni toping (ingliz tilida)',
            reply_markup=ReplyKeyboardMarkup(
                [
                    [KeyboardButton("Bosh sahifa 🏠")],
                ],
                resize_keyboard=True
            )
        )
        time.sleep(20)
    context.user_data['photo_message_id'] = sent_message.message_id
    

def handle_message(update: Update, context: CallbackContext):
    if update.message.reply_to_message:
        user_text = update.message.text
        update.message.reply_text(f"Sizning izohingiz: {user_text}")
