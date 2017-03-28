
import random
import string

#utility functions

#def a shortcode generator
def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    #this for statement is shorthand the '_' is a placeholder that isn't used but still want to run an Internationalization
    return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode(instance, size=6):
    new_code = code_generator(size=size)
    print(instance)
    print(instance.__class__)
    print(instance.__class__.__name__)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(size=size)
    return new_code
