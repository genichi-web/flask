import datetime
import flet as ft

def main(page: ft.Page):
    def do_judge(e):
        current_year = datetime.datetime.today().year #現在の西暦を取得
        kazoe_age = current_year - int(birth.value) + 1
        if sex.value == "男性" and kazoe_age in [25, 42, 61]:
            msg = f"{name.value}さん、今年、あなたは本厄ですね。"
        elif sex.value == "女性" and kazoe_age in [19, 33, 37, 61]:
            msg = f"{name.value}さん、今年、あなたは本厄ですね。"
        else:
            msg = f"{name.value}さん、今年、あなたは健やかに暮らせるでしょう。"
            
        result.value = msg
        result.update()
            
    page.title = "厄年判定"
    
    name = ft.TextField(label="お名前")
    sex = ft.Dropdown(
        label="性別",
        options=[
            ft.dropdown.Option("男性"),
            ft.dropdown.Option("女性")
        ],
    )
    birth = ft.TextField(label = "生まれ年")
    result = ft.TextField(label="判定結果", disabled=True)
    judge = ft.ElevatedButton("判定", icon="gavel", on_click=do_judge)
    
    page.add(name, sex, birth, result, judge)


ft.app(target=main, view=ft.WEB_BROWSER, port=8890)
