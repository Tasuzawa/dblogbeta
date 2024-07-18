from django_components import component

@component.register("radio")
class Radio(component.Component):
    template_name = "radio/template.html"

    class Media:
        css = "radio/style.css"
        js = "radio/script.js"
        
        


@component.register("radio-play")
class Radio_play(component.Component):
    template_name = "radio-play.html"

    class Media:
        css = "radio-play.css"
        js = "radio-play.js"


        
@component.register("table-playlist")
class table_playlist(component.Component):
    template_name = "table-playlist.html"

    class Media:
        css = "table-playlist.css"
        js = "table-playlist.js"