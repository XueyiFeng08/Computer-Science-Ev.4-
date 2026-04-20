import flet as ft

def main(page: ft.Page):
    page.title = "Quote Translator"
    page.bgcolor = "black"

    quote_text = ft.Text(
        "Perhaps there are five thousand flowers in the world just like you, but you are my one and only rose.",
        size=20,
        text_align="center",
        color="white"
    )

    author_text = ft.Text(
        "- The Little Prince (Antoine de Saint-Exupéry)",
        size=16,
        color="#d4af37",
        italic=True
    )

    def change_language(e):
        if radio.value == "en":
            quote_text.value = "Perhaps there are five thousand flowers in the world just like you, but you are my one and only rose."
        elif radio.value == "es":
            quote_text.value = "Quizás hay cinco mil flores como tú en el mundo, pero tú eres mi única rosa."
        elif radio.value == "cn":
            quote_text.value = "也许世界上也有五千朵和你一模一样的花，但只有你是我独一无二的玫瑰。"
        page.update()

    radio = ft.RadioGroup(
        value="en",
        on_change=change_language,
        content=ft.Column(
            [
                ft.Radio(value="cn", label="中文"),
                ft.Radio(value="en", label="English"),
                ft.Radio(value="es", label="Español"),
            ],
            alignment="start",
            spacing=5
        )
    )

    page.add(
        ft.Column(
            [
                quote_text,
                author_text,
                ft.Text("Choose language:", size=16, color="white"),
                radio
            ],
            horizontal_alignment="start",
            alignment="start",
            spacing=10
        )
    )

ft.app(target=main)