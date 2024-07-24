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
    images = db.get_one_model(ml)
    
    context.user_data['images'] = images
    context.user_data['photo_message_id'] = False
    length = len(images)
    c = 0
    for item in images:
        c += 1
        sent_message = update.callback_query.message.reply_photo(
            photo=item['img_url'],
            caption='Rasmni toping (ingliz tilida)',
            reply_markup=ReplyKeyboardMarkup(
                [[KeyboardButton("Bosh sahifa 🏠")]],
                resize_keyboard=True
            )
        )
        context.user_data['photo_message_id'] = sent_message.message_id
        if c!=length:
            time.sleep(10)

def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    images = context.user_data.get('images', [])
    photo_message_id = context.user_data.get('photo_message_id')
    print(images)
    for item in images:
        correct_count = 0
        incorrect_count = 0
        if photo_message_id:
            if user_message.lower() == item['name'].lower():
                text = f'{user_message} ✅'
                correct_count += 1
            else:
                text = f"{user_message} ❌({item['name']})"
                incorrect_count += 1
            update.message.reply_text(text=text)
            
    update.message.reply_text(
        text=f"To'g'ri javoblar soni: {correct_count}\nXato javoblar soni: {incorrect_count}"
    )
