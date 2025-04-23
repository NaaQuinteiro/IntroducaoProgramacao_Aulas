from shiny import reactive, render 
from shiny.express import input, ui 

ui.input_action_button("action_button", "Action")

ui.input_checkbox_group(
    "checkbox_group",
    "Teste de seleção",
    {
        "ola" : "Ola",
        "hello" : "Hello", 

    },
)

@render.text
def couter():
    return f"{input.action_button()} {input.checkbox_group()}"