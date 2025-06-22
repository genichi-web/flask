import datetime
import flet as ft

def main(page: ft.Page):
    current_year = datetime.datetime.today().year #現在の西暦を取得
    #入力値を判別して、判定ボタンを活性化する
    global name_flg, sex_flg, birth_flg
    name_flg = False
    sex_flg = False
    birth_flg = False

    def do_judge(e):
        kazoe_age = current_year - int(birth.value) + 1
        if sex.value == "男性" and kazoe_age in [25, 42, 61]:
            msg = f"{name.value}さん、今年、あなたは本厄ですね。"
        elif sex.value == "女性" and kazoe_age in [19, 33, 37, 61]:
            msg = f"{name.value}さん、今年、あなたは本厄ですね。"
        else:
            msg = f"{name.value}さん、今年、あなたは健やかに暮らせるでしょう。"
            
        result.value = msg
        result.update()
    
    def birth_check(e):
        global birth_flg
        try:
            year = int(birth.value)
            if current_year - 100 < year < current_year:
                birth_flg = True
            else:
                birth_flg = False
        except ValueError:
            birth_flg = True

        birth.update()
        judge_active()
        
    def sex_check(e):
        global sex_flg
        if not sex.value == '':
            sex_flg = True

        sex.update()
        judge_active()
        
    def name_check(e):
        global name_flg
        if not len(name.value.strip()) == 0:
            name_flg = True

        name.update()
        judge_active()
        
    def judge_active():
        judge.disabled = not (name_flg and sex_flg and birth_flg)
        judge.update()
            
    page.title = "厄年判定"
    
    name = ft.TextField(label="お名前", on_change=name_check)
    sex = ft.Dropdown(
        label="性別",
        options=[
            ft.dropdown.Option("男性"),
            ft.dropdown.Option("女性")
        ],
        on_change=sex_check
    )
    birth = ft.TextField(label = "生まれ年", on_change=birth_check)
    result = ft.TextField(label="判定結果", disabled=True)
    judge = ft.ElevatedButton("判定", disabled=True, icon="gavel", on_click=do_judge)
    
    page.add(name, sex, birth, result, judge)


ft.app(target=main, view=ft.WEB_BROWSER, port=8890)
