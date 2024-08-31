import flet as ft

def main(page: ft.Page):
    page.padding = 0
    page.window.title_bar_buttons_hidden=True
    layout = ft.Container(
        image_src="./img/cristina-gottardi-wndpWTiDuT0-unsplash.jpg",
        image_fit=ft.ImageFit.COVER,
        expand=True,
        alignment=ft.alignment.center,
        content=ft.Container(
            bgcolor=ft.colors.with_opacity(.1, ft.colors.WHITE),
            padding=ft.padding.symmetric(vertical=30, horizontal=40),
            border_radius=ft.border_radius.all(10),
            border=ft.Border(
                top=ft.BorderSide(width=2,color=ft.colors.WHITE30),
                right=ft.BorderSide(width=2,color=ft.colors.WHITE30)
            ),
            blur=ft.Blur(sigma_x=8, sigma_y=8),
            content=ft.Text(
                value='@desenvolvendocompetências',
                color=ft.colors.WHITE,
                size=30
            )
        )
    )



    page.add(layout)

if __name__ == "__main__":
    ft.app(target = main)