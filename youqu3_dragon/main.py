from nicegui import ui

from youqu3_dragon.config import config

values = {}


def get_git_url(e):
    values["git_url"] = e.value


def get_git_branch(e):
    values["git_branch"] = e.value


def get_pc_info(e):
    values["pc_info"] = e.value


def get_tags(e):
    values["tags"] = e.value


def add_tags_input():
    ui.input(
        label="用例标签",
        placeholder='CICD',
        on_change=get_tags,
        validation={'Input too long': lambda value: len(value) < 10000},
    )


def set_runway(e):
    # add_tags_input()
    ui.notify(e.value)
    # values["runway"] = e.value


def run_youqu_cmd():
    # os.system("pip install youqu3")
    # os.system("youqu3-envx")
    print(f"youqu3-cargo run -t {values['tags']}")


(ui.image("https://img-s-msn-com.akamaized.net/tenant/amp/entityid/BB1msKEv.img")
 .tailwind
 .background_position("center")
 .background_attachment("fixed")
 .background_size("cover"))

with ui.card().style(
        "width: 400px;"
        "position:absolute;"
        "left:50%;"
        "margin-left: -100px;"
        "top:50%;"
        "margin-top: -100px;"
):
    ui.input(
        label="用例仓库",
        placeholder='ssh://ut001203@gerrit.uniontech.com:29418/autotest_deepin_music',
        on_change=get_git_url,
        validation={'Input too long': lambda value: len(value) < 10000},
    )
    ui.input(
        label="分支",
        autocomplete=['at-develop/eagle'],
        on_change=get_git_branch,
        validation={'Input too long': lambda value: len(value) < 10000},
    )
    ui.input(
        label="测试机信息",
        placeholder='uos@10.8.13.11',
        on_change=get_pc_info,
        validation={'Input too long': lambda value: len(value) < 10000},
    )

    with ui.tabs().classes('w-full') as tabs:
        one = ui.tab('One')
        two = ui.tab('Two')
    with ui.tab_panels(tabs, value=two).classes('w-full'):
        with ui.tab_panel(one):
            ui.label('First tab')
        with ui.tab_panel(two):
            ui.label('Second tab')


    ui.button(
        "YouQu3",
        on_click=run_youqu_cmd,
    ).style("display:block;margin: 0 auto;")

ui.run(
    title="YouQu3 Dragon",
    favicon=config.root_dir / "favicon.ico"
)
