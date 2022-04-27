from wifipumpkin3.plugins.captiveflask.plugin import CaptiveTemplatePlugin
import wifipumpkin3.core.utility.constants as C # import plugin class base

class ExamplePlugin(CaptiveTemplatePlugin):
    meta = {
        'Name'      : 'ExamplePlugin',
        'Version'   : '1.0',
        'Description' : 'Example is a simple portal default page',
        'Author'    : ' the Author',
        'TemplatePath' : C.TEMPLATES_FLASK +'templates/ExamplePlugin',
        'StaticPath' : C.TEMPLATES_FLASK + 'templates/ExamplePlugin/static',
        'Preview' : 'plugins/captivePortal/templates/ExamplePlugin/preview.png'
    }

    def __init__(self):
        for key,value in self.meta.items():
            self.__dict__[key] = value
        self.dict_domain = {}
        self.ConfigParser = False 