def my_simple_ui():
    imgui.begin("Example Window")
    
    imgui.text("This is a simple UI without anything inside.")
    imgui.text("You can add your logic here!")
    
    imgui.end()

clear_uis()
add_ui("SimpleExample", my_simple_ui)
log("Simple UI loaded.")
while True:
    sleep(1.0)
