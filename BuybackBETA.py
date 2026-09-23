import tkinter as tk
from tkinter import messagebox, ttk

# ---- Палитра ----
BG        = "#1E1E2E"
CARD      = "#2A2A3C"
ACCENT    = "#7C5CFF"
ACCENT_H  = "#9277FF"
TEXT      = "#EAEAF0"
MUTED     = "#A0A0B0"
SUCCESS   = "#4ADE80"
DANGER    = "#F87171"
DIVIDER   = "#3A3A4C"

# ---- Константы формулы ----
BASE = 200
MULTIPLIER = 13

# ---- Переводы ----
TRANSLATIONS = {
    "ru": {
        "title": "Теорема Байбэка", "window": "Теорема Байбэка",
        "label_input": "Цена байбэка", "button": "Рассчитать нетворс",
        "label_result": "Твой нетворс", "lang_label": "Язык",
        "warn_empty": "Введите цену байбэка!", "warn_title": "Внимание",
        "err_title": "Ошибка", "err_number": "Введите корректное число!",
    },
    "en": {
        "title": "Buyback Theorem", "window": "Buyback Theorem",
        "label_input": "Buyback price", "button": "Calculate net worth",
        "label_result": "Your net worth", "lang_label": "Language",
        "warn_empty": "Enter the buyback price!", "warn_title": "Warning",
        "err_title": "Error", "err_number": "Please enter a valid number!",
    },
    "uk": {
        "title": "Теорема Байбеку", "window": "Теорема Байбеку",
        "label_input": "Ціна байбеку", "button": "Розрахувати нетворс",
        "label_result": "Твій нетворс", "lang_label": "Мова",
        "warn_empty": "Введи ціну байбеку!", "warn_title": "Увага",
        "err_title": "Помилка", "err_number": "Введи коректне число!",
    },
    "be": {
        "title": "Тэарэма Байбэка", "window": "Тэарэма Байбэка",
        "label_input": "Цана байбэка", "button": "Разлічыць нэтворс",
        "label_result": "Твой нэтворс", "lang_label": "Мова",
        "warn_empty": "Увядзіце цану байбэка!", "warn_title": "Увага",
        "err_title": "Памылка", "err_number": "Увядзіце карэктны лік!",
    },
    "es": {
        "title": "Teorema del Buyback", "window": "Teorema del Buyback",
        "label_input": "Precio del buyback", "button": "Calcular patrimonio",
        "label_result": "Tu patrimonio", "lang_label": "Idioma",
        "warn_empty": "¡Introduce el precio del buyback!", "warn_title": "Atención",
        "err_title": "Error", "err_number": "¡Introduce un número válido!",
    },
    "de": {
        "title": "Buyback-Theorem", "window": "Buyback-Theorem",
        "label_input": "Buyback-Preis", "button": "Vermögen berechnen",
        "label_result": "Dein Vermögen", "lang_label": "Sprache",
        "warn_empty": "Bitte Buyback-Preis eingeben!", "warn_title": "Hinweis",
        "err_title": "Fehler", "err_number": "Bitte eine gültige Zahl eingeben!",
    },
    "it": {
        "title": "Teorema del Buyback", "window": "Teorema del Buyback",
        "label_input": "Prezzo del buyback", "button": "Calcola patrimonio",
        "label_result": "Il tuo patrimonio", "lang_label": "Lingua",
        "warn_empty": "Inserisci il prezzo del buyback!", "warn_title": "Attenzione",
        "err_title": "Errore", "err_number": "Inserisci un numero valido!",
    },
    "fr": {
        "title": "Théorème du Buyback", "window": "Théorème du Buyback",
        "label_input": "Prix du buyback", "button": "Calculer le patrimoine",
        "label_result": "Ton patrimoine", "lang_label": "Langue",
        "warn_empty": "Entrez le prix du buyback !", "warn_title": "Attention",
        "err_title": "Erreur", "err_number": "Entrez un nombre valide !",
    },
    "pt": {
        "title": "Teorema do Buyback", "window": "Teorema do Buyback",
        "label_input": "Preço do buyback", "button": "Calcular patrimônio",
        "label_result": "Seu patrimônio", "lang_label": "Idioma",
        "warn_empty": "Insira o preço do buyback!", "warn_title": "Atenção",
        "err_title": "Erro", "err_number": "Insira um número válido!",
    },
    "ar": {
        "title": "نظرية الباي باك", "window": "نظرية الباي باك",
        "label_input": "سعر الباي باك", "button": "احسب الثروة",
        "label_result": "ثروتك", "lang_label": "اللغة",
        "warn_empty": "أدخل سعر الباي باك!", "warn_title": "تنبيه",
        "err_title": "خطأ", "err_number": "أدخل رقمًا صحيحًا!",
    },
    "he": {
        "title": "משפט הבייבק", "window": "משפט הבייבק",
        "label_input": "מחיר הבייבק", "button": "חשב שווי נטו",
        "label_result": "שווי נטו שלך", "lang_label": "שפה",
        "warn_empty": "הזן את מחיר הבייבק!", "warn_title": "אזהרה",
        "err_title": "שגיאה", "err_number": "הזן מספר תקין!",
    },
    "zh": {
        "title": "回购定理", "window": "回购定理",
        "label_input": "回购价格", "button": "计算净资产",
        "label_result": "你的净资产", "lang_label": "语言",
        "warn_empty": "请输入回购价格！", "warn_title": "提示",
        "err_title": "错误", "err_number": "请输入有效的数字！",
    },
    "fi": {
        "title": "Buyback-lause", "window": "Buyback-lause",
        "label_input": "Buyback-hinta", "button": "Laske nettovarallisuus",
        "label_result": "Nettovarallisuutesi", "lang_label": "Kieli",
        "warn_empty": "Syötä buyback-hinta!", "warn_title": "Huomio",
        "err_title": "Virhe", "err_number": "Syötä kelvollinen luku!",
    },
}

# (код, отображаемое название)
LANGUAGES = [
    ("ru", "Русский"),
    ("en", "English"),
    ("uk", "Українська"),
    ("be", "Беларуская"),
    ("es", "Español"),
    ("de", "Deutsch"),
    ("it", "Italiano"),
    ("fr", "Français"),
    ("pt", "Português"),
    ("ar", "العربية"),
    ("he", "עברית"),
    ("zh", "中文"),
    ("fi", "Suomi"),
]

current_lang = "ru"


def t(key):
    return TRANSLATIONS[current_lang].get(key, key)


def calculate_networth():
    raw = entry.get().strip().replace(",", ".")
    if not raw:
        messagebox.showwarning(t("warn_title"), t("warn_empty"))
        return
    try:
        buyback = float(raw)
    except ValueError:
        messagebox.showerror(t("err_title"), t("err_number"))
        return

    networth = (buyback - BASE) * MULTIPLIER

    if networth.is_integer():
        text = f"{int(networth):,}".replace(",", " ")
    else:
        text = f"{networth:,.2f}".replace(",", " ")

    color = SUCCESS if networth >= 0 else DANGER
    result_label.config(text=text, fg=color)


def on_enter(_): btn.config(bg=ACCENT_H)
def on_leave(_): btn.config(bg=ACCENT)
def clear_entry(_): entry.delete(0, tk.END)


def apply_language():
    root.title(t("window"))
    title_label.config(text=t("title"))
    label_input.config(text=t("label_input"))
    btn.config(text=t("button"))
    label_result.config(text=t("label_result"))
    lang_label.config(text=t("lang_label"))


def on_lang_change(event=None):
    global current_lang
    selected = lang_combo.get()
    for code, name in LANGUAGES:
        if name == selected:
            current_lang = code
            break
    apply_language()


# ---- Окно ----
root = tk.Tk()
root.configure(bg=BG)
root.resizable(False, False)

card = tk.Frame(root, bg=CARD, padx=40, pady=30)
card.pack(padx=20, pady=20, fill="both", expand=True)

title_label = tk.Label(card, text=t("title"),
                       font=("Segoe UI", 20, "bold"),
                       bg=CARD, fg=TEXT)
title_label.pack(pady=(0, 25))

label_input = tk.Label(card, text=t("label_input"),
                       font=("Segoe UI", 11),
                       bg=CARD, fg=MUTED)
label_input.pack(anchor="w")

entry_wrap = tk.Frame(card, bg=ACCENT, padx=2, pady=2)
entry_wrap.pack(fill="x", pady=(4, 20))

entry = tk.Entry(entry_wrap,
                 font=("Segoe UI", 16),
                 bg=BG, fg=TEXT,
                 insertbackground=TEXT,
                 relief="flat",
                 justify="center",
                 width=18)
entry.pack(ipady=8)
entry.bind("<Return>", lambda e: calculate_networth())
entry.bind("<FocusIn>", clear_entry)

btn = tk.Button(card, text=t("button"),
                font=("Segoe UI", 12, "bold"),
                bg=ACCENT, fg="white",
                activebackground=ACCENT_H, activeforeground="white",
                relief="flat", bd=0, cursor="hand2",
                command=calculate_networth)
btn.pack(fill="x", ipady=10, pady=(0, 25))
btn.bind("<Enter>", on_enter)
btn.bind("<Leave>", on_leave)

label_result = tk.Label(card, text=t("label_result"),
                        font=("Segoe UI", 11),
                        bg=CARD, fg=MUTED)
label_result.pack()

result_label = tk.Label(card, text="0",
                        font=("Segoe UI", 28, "bold"),
                        bg=CARD, fg=SUCCESS)
result_label.pack(pady=(4, 0))

# --- Нижний блок: разделитель + язык ---
divider = tk.Frame(card, bg=DIVIDER, height=1)
divider.pack(fill="x", pady=(25, 15))

lang_row = tk.Frame(card, bg=CARD)
lang_row.pack()

lang_label = tk.Label(lang_row, text=t("lang_label"),
                      font=("Segoe UI", 10),
                      bg=CARD, fg=MUTED)
lang_label.pack(side="left", padx=(0, 10))

# Стилизация Combobox
style = ttk.Style()
style.theme_use("clam")
style.configure("Lang.TCombobox",
                fieldbackground=BG,
                background=BG,
                foreground=TEXT,
                arrowcolor=MUTED,
                bordercolor=BG,
                lightcolor=BG,
                darkcolor=BG,
                padding=4)
style.map("Lang.TCombobox",
          fieldbackground=[("readonly", BG)],
          foreground=[("readonly", TEXT)],
          bordercolor=[("focus", ACCENT)])

lang_combo = ttk.Combobox(lang_row,
                          values=[name for _, name in LANGUAGES],
                          state="readonly",
                          width=16,
                          font=("Segoe UI", 10),
                          style="Lang.TCombobox")
lang_combo.set(LANGUAGES[0][1])
lang_combo.pack(side="left")
lang_combo.bind("<<ComboboxSelected>>", on_lang_change)

entry.focus_set()
root.mainloop()