from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Малакаҳо", callback_data="skills")],
    [InlineKeyboardButton(text="Проектҳо", callback_data="projects")],
    [InlineKeyboardButton(text="Контакт", callback_data="contact")]
])