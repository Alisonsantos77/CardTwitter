import flet as ft


def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    avatar = ft.Image(
        col=2,
        src='avatar.png',
        height=70,
        width=70,
    )
    user = ft.Text(
        spans=[
            ft.TextSpan(text='Python_Brasil',
                        style=ft.TextStyle(color=ft.colors.BLACK, weight=ft.FontWeight.BOLD)),
            ft.TextSpan(text=' @pythonbrasil', style=ft.TextStyle(color=ft.colors.GREY)),
        ],
        size=16,

    )
    description = ft.Text(value='Você é a média das 5 pessoas que mais convive, e o servidor dá a oportunidade de '
                                'você colocar apenas as melhores pessoas do seu lado.', color=ft.colors.BLACK
                          )
    media = ft.Container(
        border_radius=ft.border_radius.all(20),
        border=ft.border.all(width=1, color=ft.colors.GREY_300),
        margin=ft.margin.symmetric(vertical=10),
        content=ft.Column(
            spacing=0,
            controls=[
                ft.Image(
                    src='post.jpg',
                    fit=ft.ImageFit.COVER,
                    aspect_ratio=1.78,  # 16/9

                ),
                ft.Container(
                    padding=ft.padding.all(20),
                    content=ft.Column(
                        spacing=0,
                        controls=[
                            user,
                            ft.Text(
                                value='Mantenha os pés no seu sonho!😎', color=ft.colors.BLACK,
                                max_lines=1,
                                overflow=ft.TextOverflow.ELLIPSIS,
                            )
                        ]
                    )
                )
            ]
        )
    )
    actions = ft.ResponsiveRow(
        controls=[
            ft.Icon(name=ft.icons.CHAT, col=1, color=ft.colors.BLACK),
            ft.Icon(name=ft.icons.SHARE, col=1, color=ft.colors.BLACK),
            ft.Icon(name=ft.icons.FAVORITE_BORDER, col=1, color=ft.colors.BLACK),
            ft.Icon(name=ft.icons.ANALYTICS, col=1, color=ft.colors.BLACK)
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    layout = ft.Container(
        # height=700,
        width=500,
        bgcolor=ft.colors.WHITE,
        border_radius=ft.border_radius.all(10),
        padding=ft.padding.all(20),
        shadow=ft.BoxShadow(color=ft.colors.LIGHT_BLUE_ACCENT, blur_radius=300),
        content=ft.ResponsiveRow(
            controls=[
                avatar,
                ft.Column(
                    col=10,
                    controls=[
                        user,
                        description,
                        media,
                        actions,
                    ]

                )
            ]
        )
    )

    page.add(layout)


if __name__ == '__main__':
    ft.app(target=main)
