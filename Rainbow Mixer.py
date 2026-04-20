import flet as ft

def main(page: ft.Page):

    def changeColor(e):
        r = int(redSlider.value)
        g = int(greenSlider.value)
        b = int(blueSlider.value)

        color = f"#{r:02x}{g:02x}{b:02x}"

        colorText.value = f"RGB({r}, {g}, {b})"

        page.bgcolor = color

    redSlider = ft.Slider(label="Red", value=0, min=0, max=255, divisions=255, on_change=changeColor)
    greenSlider = ft.Slider(label="Green", value=0, min=0, max=255, divisions=255, on_change=changeColor)
    blueSlider = ft.Slider(label="Blue", value=0, min=0, max=255, divisions=255, on_change=changeColor)

    colorText = ft.Text(value="RGB(0, 0, 0)")

    page.add(colorText, redSlider, greenSlider, blueSlider)

ft.run(main=main)