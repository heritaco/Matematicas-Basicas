import pyperclip
import re

# Obtiene el texto del portapapeles
texto = pyperclip.paste()

# Expresión regular para reemplazar cualquier i.j al inicio del título
resultado = re.sub(r'(\\subsection\{)\d+\.\d+\s+', r'\1', texto)

pyperclip.copy(resultado)
print("El resultado ha sido copiado al portapapeles.")
