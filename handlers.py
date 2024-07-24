from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CallbackContext
import keyboards
import db
import random
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
<<<<<<< HEAD
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
=======
    context.user_data['current_image_index'] = 0
    context.user_data['correct_count'] = 0
    context.user_data['incorrect_count'] = 0

    send_next_image(update, context)

def send_next_image(update: Update, context: CallbackContext):
    images = context.user_data.get('images', [])
    current_index = context.user_data.get('current_image_index', 0)

    if current_index < len(images):
        item = images[current_index]
        image_ls = [j['name'] for j in images if j['name'] != item['name']]
        random_image = random.sample(image_ls, 3)
        btns = [
            InlineKeyboardButton(item['name'], callback_data=f'answer:{current_index}:True'), 
            InlineKeyboardButton(random_image[0], callback_data=f'answer:{current_index}:False'),
            InlineKeyboardButton(random_image[1], callback_data=f'answer:{current_index}:False'),
            InlineKeyboardButton(random_image[2], callback_data=f'answer:{current_index}:False')
        ]
        random.shuffle(btns)
        reply_markup = InlineKeyboardMarkup(
            [
                btns[:2],
                btns[2:]
            ]
        )

        if update.callback_query:
            sent_message = update.callback_query.message.reply_photo(
                photo=item['img_url'],
                caption='Rasmni toping (ingliz tilida)',
                reply_markup=reply_markup
            )
        else:
            sent_message = update.message.reply_photo(
                photo=item['img_url'],
                caption='Rasmni toping (ingliz tilida)',
                reply_markup=reply_markup
            )

        context.user_data['current_image_index'] += 1
    else:
        send_report(update, context)

def answer_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data.split(':')
    current_index = int(data[1])
    is_correct = data[2] == 'True'

    if is_correct:
        context.user_data['correct_count'] += 1
        query.answer(text="To'g'ri javob!")
    else:
        context.user_data['incorrect_count'] += 1
        query.answer(text="Noto'g'ri javob!")

    send_next_image(update, context)

def send_report(update: Update, context: CallbackContext):
    correct_count = context.user_data.get('correct_count', 0)
    incorrect_count = context.user_data.get('incorrect_count', 0)

    report_text = f"To'g'ri javoblar soni: {correct_count} ✅\nXato javoblar soni: {incorrect_count} ❌"

    update.callback_query.message.reply_text(
        text=report_text,
        reply_markup=ReplyKeyboardMarkup(
            [[KeyboardButton(text='Bosh sahifa 🏠')]],
            resize_keyboard=True
        )
        )
>>>>>>> bb1dadbeef563c00f74e3854ee3afce1c29d0735
