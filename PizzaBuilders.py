import flet as ft

def main(page: ft.Page):

    def update_pizza(e):
        pepperoniImage.visible = pepperoniSwitch.value

        mushroom1.visible = mushroomSwitch.value
        mushroom2.visible = mushroomSwitch.value
        mushroom3.visible = mushroomSwitch.value
        mushroom4.visible = mushroomSwitch.value
        mushroom5.visible = mushroomSwitch.value

        olive1.visible = oliveSwitch.value
        olive2.visible = oliveSwitch.value
        olive3.visible = oliveSwitch.value
        olive4.visible = oliveSwitch.value
        olive5.visible = oliveSwitch.value

        pepper1.visible = pepperSwitch.value
        pepper2.visible = pepperSwitch.value
        pepper3.visible = pepperSwitch.value
        pepper4.visible = pepperSwitch.value
        pepper5.visible = pepperSwitch.value

        page.update()

    page.window.width = 900
    page.window.height = 700
    page.title = "Pizza Builder"

    basePizza = ft.Image(
        src="base_pizza.png",
        width=500,
        height=500
    )

    pepperoniImage = ft.Image(
        src="pepperoni.png",
        width=500,
        height=500,
        visible=False
    )

    mushroom1 = ft.Image(src="mushroom.png", width=110, height=110, top=80, left=120, visible=False)
    mushroom2 = ft.Image(src="mushroom.png", width=105, height=105, top=180, left=300, visible=False)
    mushroom3 = ft.Image(src="mushroom.png", width=110, height=110, top=300, left=200, visible=False)
    mushroom4 = ft.Image(src="mushroom.png", width=100, height=100, top=140, left=270, visible=False)
    mushroom5 = ft.Image(src="mushroom.png", width=105, height=105, top=250, left=90, visible=False)

    olive1 = ft.Image(src="olive.png", width=85, height=85, top=110, left=250, visible=False)
    olive2 = ft.Image(src="olive.png", width=80, height=80, top=230, left=150, visible=False)
    olive3 = ft.Image(src="olive.png", width=85, height=85, top=320, left=300, visible=False)
    olive4 = ft.Image(src="olive.png", width=80, height=80, top=170, left=200, visible=False)
    olive5 = ft.Image(src="olive.png", width=85, height=85, top=260, left=60, visible=False)

    pepper1 = ft.Image(src="peppers.png", width=90, height=90, top=120, left=100, visible=False)
    pepper2 = ft.Image(src="peppers.png", width=85, height=85, top=260, left=260, visible=False)
    pepper3 = ft.Image(src="peppers.png", width=90, height=90, top=330, left=120, visible=False)
    pepper4 = ft.Image(src="peppers.png", width=85, height=85, top=180, left=350, visible=False)
    pepper5 = ft.Image(src="peppers.png", width=90, height=90, top=80, left=250, visible=False)

    pizzaStack = ft.Stack(
        width=500,
        height=500,
        controls=[
            basePizza,
            pepperoniImage,

            mushroom1, mushroom2, mushroom3, mushroom4, mushroom5,

            olive1, olive2, olive3, olive4, olive5,

            pepper1, pepper2, pepper3, pepper4, pepper5
        ]
    )

    pepperoniSwitch = ft.Switch(label="Pepperoni", on_change=update_pizza)
    mushroomSwitch = ft.Switch(label="Mushrooms", on_change=update_pizza)
    oliveSwitch = ft.Switch(label="Olives", on_change=update_pizza)
    pepperSwitch = ft.Switch(label="Peppers", on_change=update_pizza)

    controlsColumn = ft.Column(
        controls=[
            ft.Text("Choose your toppings", size=20, weight="bold"),
            pepperoniSwitch,
            mushroomSwitch,
            oliveSwitch,
            pepperSwitch
        ]
    )

    page.add(
        ft.Row(
            controls=[
                pizzaStack,
                controlsColumn
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.run(main)