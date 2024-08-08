from django.forms.widgets import (
    TextInput,
    PasswordInput,
    EmailInput,
)

class BaseInput:
    def __init__(self, *args, **kwargs):
        default_attrs = {
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg '
                     'focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 '
                     'dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 '
                     'dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
        }
        # Merge provided attrs with default attrs
        if 'attrs' in kwargs:
            default_attrs.update(kwargs['attrs'])
        kwargs['attrs'] = default_attrs
        super().__init__(*args, **kwargs)

class CustomTextInput(BaseInput, TextInput):
    pass

class CustomPasswordInput(BaseInput, PasswordInput):
    pass

class CustomEmailInput(BaseInput, EmailInput):
    pass
