def get_prompt_for_fidelity(context, actual_answer):
    return f"""Según la sentencia y el contexto proporcionado, genere un objeto JSON para indicar si la sentencia está basada en hechos fácticos presentes en el contexto. El JSON tendrá 1 único campo obligatorio: 'value'.
El valor del 'value' debe ser ESTRICTAMENTE un número de 1 a 10, siendo 1 no basada en el contexto y 10 muy basada en el context.

**
IMPORTANTE: asegúrese de devolver solo en formato JSON.
Contexto de ejemplo: ["Einstein ganó el Premio Nobel por su descubrimiento del efecto fotoeléctrico", "Ganó el Premio Nobel en 1968", "Había un gato"]
Sentencia de ejemplo: "Albert Einstein gano un premio nobel gracias a los garos"

Salida de ejemplo:
{{
     "value": "0"
}}
**

Sentencia:
{actual_answer}

Contexto:
{context}

JSON:
"""



def get_prompt_for_relevancy(question, actual_answer):
    return f"""Según la pregunta y la respuesta proporcionado, genere un objeto JSON para indicar si la respuesta tiene sentido en relación a la pregunta. El JSON tendrá 1 único campo obligatorio: 'value'.
El valor del 'value' debe ser ESTRICTAMENTE un número de 1 a 10, siendo 1 sin sentido y 10 con mucho sentido.

**
IMPORTANTE: asegúrese de devolver solo en formato JSON.
Pregunta de ejemplo: "¿Es posible hacer una ensalada de un solo ingrediente?"
Respuesta de ejemplo: "Los ingredientes que elijas determinarán la calidad de tu comida"

Salida de ejemplo:
{{
     "value": "2"
}}
**

Pregunta:
{question}

Respuesta:
{actual_answer}


JSON:
"""


def get_prompt_for_accurancy(question, context):
    return f"""Según la pregunta y el contexto proporcionado, genere un objeto JSON para indicar si el contexto proporcionado es útil para responder a la pregunta. El JSON tendrá 1 único campo obligatorio: 'value'.
El valor del 'value' debe ser ESTRICTAMENTE un número de 1 a 10, siendo 1 nada útil y 10 muy útil.

**
IMPORTANTE: asegúrese de devolver solo en formato JSON.
Pregunta de ejemplo: "¿Es posible hacer una ensalada de un solo ingrediente?"
Contexto de ejemplo: ["Los ingredientes que elijas determinarán la calidad de tu comida", "Una ensalada debe tener tomate", "Para preparar una pizza se necesita harina"]

Salida de ejemplo:
{{
     "value": "5"
}}
**

Pregunta:
{question}

Contexto:
{context}


JSON:
"""