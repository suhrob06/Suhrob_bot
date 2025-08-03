from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from states import ContactForm
from keyboards import main_menu
from config import ADMIN_CHAT_ID

router = Router()

# Start command
@router.message(F.text == "/start")
async def start_handler(message: Message):
    text = (
        "Салом, дӯстам! Ман <b>Боти Сухроб</b> ҳастам 🤖✨\n\n"
        "Ман як фрилансер ва барномасози вебу ботҳо мебошам.\n"
        "Аз меню яке аз қисматҳоро интихоб намо, то шиносоии бештар пайдо кунӣ! 👇"
    )
    await message.answer(text, reply_markup=main_menu, parse_mode="HTML")

# Skills menu handler
@router.callback_query(F.data == "skills")
async def skills_handler(callback: CallbackQuery):
    skills_text = (
        "🚀 <b>Малакаҳои ман</b>:\n\n"
        "🧠 Python — таҳияи скрипт ва веб-аппҳо\n"
        "🤖 Telegram Bot — бо Aiogram 3.x\n"
        "🌐 HTML, CSS, JavaScript — веб-дизайн ва интерфейс\n"
        "⚙️ Автоматизатсия — коркарди вазифаҳои худкор\n\n"
        "📌 Барои шиносоӣ бо корҳоям, лутфан «Проектҳо»-ро аз меню пахш кун! 😊"
    )
    await callback.message.answer(skills_text, reply_markup=main_menu, parse_mode="HTML")
    await callback.answer()

# Projects menu handler
@router.callback_query(F.data == "projects")
async def projects_handler(callback: CallbackQuery):
    projects_text = (
        "📁 <b>Намунаи проектҳои ман:</b>\n\n"
        "1️⃣ <a href='https://t.me/SuhrobHelpBot'>Telegram боти фриланс</a>\n"
        "2️⃣ <a href='https://suhrob06.github.io/freelancer_bot/'>Сомонаи шахсӣ</a>\n"
        "3️⃣ Автоматизатсияи бизнес ва дигар скриптҳои муфид\n\n"
        "📞 Агар хоҳӣ бо ман тамос гирӣ, дар меню тугмаи «Контакт»-ро пахш кун."
    )
    await callback.message.answer(
        projects_text,
        reply_markup=main_menu,
        parse_mode="HTML",
        disable_web_page_preview=True
    )
    await callback.answer()

# Contact menu handler
@router.callback_query(F.data == "contact")
async def contact_handler(callback: CallbackQuery, state: FSMContext):
    contact_info = (
        "📲 <b>Тамос бо ман</b>\n\n"
        "🔹 Telegram: <a href='https://t.me/odilmatov_o6'>@odilmatov_o6</a>\n"
        "✍️ Агар хоҳӣ паёми шахсӣ нависӣ — танҳо паёматро навис ва ман онро бо хушнудӣ қабул мекунам! 😊"
    )
    await callback.message.answer(contact_info, parse_mode="HTML", disable_web_page_preview=True)
    await state.set_state(ContactForm.waiting_for_message)
    await callback.answer()

# Processing user's personal message
@router.message(ContactForm.waiting_for_message)
async def process_user_message(message: Message, state: FSMContext):
    user_message = message.text
    user_name = message.from_user.full_name
    username = message.from_user.username or "Неизвестен"

    # Sending user's message to admin
    try:
        await message.bot.send_message(
            ADMIN_CHAT_ID,
            f"📩 Паёми нав аз @{username} ({user_name}):\n\n{user_message}"
        )
    except Exception as e:
        # Агар паём ба админ наравад, хатогиро лог кун ва ба корбар хабар деҳ
        await message.answer("Мушкилот дар ирсоли паём ба админ. Лутфан баъдтар кӯшиш кунед.")
        await state.clear()
        return

    # Replying to user
    await message.answer("✅ Паёматон бо муваффақият ирсол шуд! Ба зудӣ ҷавоб хоҳам дод 🙌")
    await state.clear()