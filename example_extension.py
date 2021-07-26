import vscode

ext = vscode.Extension(name="testpy", display_name="Test Py", version = "0.0.1")

@ext.event
def on_activate():
    return f"The Extension '{ext.name}' has started"

@ext.command()
def hello_world():
    return vscode.window.show_info_message(f'Hello World from {ext.name}')

@ext.command()
def ask_question():
    res = vscode.window.show_info_message('How are you?', 'Great', 'Meh')
    if res == "Great":
        vscode.window.show_info_message('Woah nice!!')
    elif res == "Meh":
        vscode.window.show_info_message('Sorry to hear that :(')

@ext.command()
def show_picker():
    data = [
        {
            'label': 'apple',
            'detail': 'A fruit'
        }, 
        {
            'label': 'boring',
            'detail': 'An adjective'            
        }
    ]
    res = vscode.window.show_quick_pick(data, {'matchOnDetail': True})
    vscode.window.show_info_message(f"Nice you chose {res['label']}")
    
vscode.build(ext)
